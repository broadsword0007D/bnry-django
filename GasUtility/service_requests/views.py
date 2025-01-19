from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from .models import ServiceRequest
from .forms import ServiceRequestForm


def request_list(request):
    """
    List all service requests for the currently logged-in user.
    If the user is staff (e.g., a customer support rep), list all requests.
    """
    if request.user.is_staff:  # or check for another role if you have a custom user model
        requests_qs = ServiceRequest.objects.all().order_by('-created_at')
    else:
        requests_qs = ServiceRequest.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'service_requests/request_list.html', {
        'requests': requests_qs
    })


def request_detail(request, pk):
    """
    Display details for a specific service request.
    """
    sr = get_object_or_404(ServiceRequest, pk=pk)
    # Ensure non-staff can only see their own requests
    if not request.user.is_staff and sr.user != request.user:
        messages.error(request, "You do not have permission to view this request.")
        return redirect('service_requests:request_list')

    return render(request, 'service_requests/request_detail.html', {
        'request_obj': sr
    })


def request_create(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user  # Associate the request with the logged-in user
            service_request.save()
            messages.success(request, "Service request submitted successfully!")
            return redirect('service_requests:request_list')  # Redirect to the list of service requests
    else:
        form = ServiceRequestForm()

    return render(request, 'service_requests/request_create.html', {'form': form})


def request_update(request, pk):
    """
    Update existing service request. Typically, only staff or the request owner can do this.
    """
    sr = get_object_or_404(ServiceRequest, pk=pk)
    if not request.user.is_staff and sr.user != request.user:
        messages.error(request, "You do not have permission to edit this request.")
        return redirect('service_requests:request_list')

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES, instance=sr)
        if form.is_valid():
            sr = form.save()
            messages.success(request, "Service Request Updated Successfully!")
            return redirect('service_requests:request_detail', pk=pk)
    else:
        form = ServiceRequestForm(instance=sr)
    return render(request, 'service_requests/request_create.html', {
        'form': form,
        'update': True
    })


def manage_requests(request):
    """
    A view for customer support representatives (staff) to manage requests:
    - Mark them as In Progress, Resolved, etc.
    - Possibly assign them to different support reps
    """
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to manage requests.")
        return redirect('service_requests:request_list')

    requests_qs = ServiceRequest.objects.all().order_by('-created_at')

    if request.method == 'POST':
        action = request.POST.get('action')
        sr_id = request.POST.get('sr_id')
        sr = get_object_or_404(ServiceRequest, pk=sr_id)
        
        if action == 'in_progress':
            sr.status = ServiceRequest.IN_PROGRESS
        elif action == 'resolved':
            sr.status = ServiceRequest.RESOLVED
            sr.resolved_at = timezone.now()
        elif action == 'closed':
            sr.status = ServiceRequest.CLOSED
        
        sr.save()
        messages.success(request, f"Request #{sr.id} updated to {sr.status}.")

    return render(request, 'service_requests/manage_requests.html', {
        'requests': requests_qs
    })
