# Gas Utility Service Portal

This Django application provides a portal for gas utility customers to submit, track, and manage service requests online. It also includes tools for customer support representatives to manage and resolve these requests efficiently.

## Features

### For Customers
- **Submit Service Requests**: Customers can create service requests online, specifying the request type, description, and attaching files if necessary.
- **Track Service Requests**: Customers can view the status of their service requests, including submission and resolution dates.
- **Profile Management**: Customers can log in to their accounts and manage their personal information.

### For Customer Support Representatives
- **Manage Service Requests**: View, update, and resolve service requests.
- **Role-Based Access**: Differentiate actions available to customers and support staff.

---

## Project Structure

```
GasUtility/
├── manage.py                  # Django management script
├── GasUtility/                # Project settings and configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Main settings file
│   ├── urls.py                # URL configurations
│   └── wsgi.py
├── accounts/                  # App for user authentication and profiles
│   ├── templates/accounts/    # Templates for accounts-related pages
│   │   ├── login.html
│   │   ├── profile.html
│   │   └── logout.html
│   ├── models.py              # User profile extensions
│   ├── views.py               # Views for login, logout, and profile
│   ├── urls.py                # URL configurations for accounts
│   └── forms.py               # Forms for user authentication
├── service_requests/          # App for managing service requests
│   ├── templates/service_requests/
│   │   ├── request_create.html
│   │   ├── request_list.html
│   │   └── request_detail.html
│   ├── models.py              # ServiceRequest model
│   ├── views.py               # Views for CRUD operations on requests
│   ├── urls.py                # URL configurations for requests
│   └── forms.py               # Forms for service request submission
├── templates/                 # Global templates folder
│   └── home.html              # Homepage template
└── static/                    # Static files (CSS, JS, images)
```

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A virtual environment tool (optional but recommended)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo-name/gas-utility-service.git
   cd gas-utility-service
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Usage

### Homepage
The homepage provides navigation links to:
- Login
- View service requests
- Create a new service request

### Submitting a Service Request
1. Navigate to `http://127.0.0.1:8000/requests/create/`.
2. Fill out the form with the request type, description, and any optional attachments.
3. Submit the form to save the request.

### Viewing Service Requests
1. Navigate to `http://127.0.0.1:8000/requests/`.
2. View the list of all your submitted service requests.
3. Click on a request to view its details.

### Customer Support
Customer support representatives can log in to manage and resolve service requests.

---

## Key Files

### Models
- **`ServiceRequest`** (in `service_requests/models.py`): Represents a customer service request.
- **`Profile`** (in `accounts/models.py`): Extends the user model for additional customer information.

### Views
- **`request_create`**: Handles submission of new service requests.
- **`request_list`**: Lists all requests for the logged-in user.
- **`request_detail`**: Shows detailed information about a specific request.

### Templates
- **`home.html`**: The main landing page.
- **`request_create.html`**: Form for submitting service requests.
- **`request_list.html`**: Displays a list of service requests.

---

## Future Enhancements
- Notifications for customers when their request status changes.
- Admin dashboard with analytics on service requests.
- File upload validation and size restrictions.

---

## License
This project is licensed under the MIT License.

---

## Contributing
Feel free to fork this repository and submit pull requests with improvements or bug fixes. Contributions are welcome!
