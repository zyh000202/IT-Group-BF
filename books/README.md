# Library Management System

A simple web-based library management system built with Django as part of a university coursework project. It allows users to browse, borrow, and return books, while administrators can manage the book catalog.

## Features

- User authentication (register, login, logout)
- Browse books with search and category filtering
- View book details (title, author, ISBN, availability, etc.)
- Borrow and return books with AJAX (no page reload)
- Personal borrow history and current loans
- Admin interface for adding, editing, and deleting books
- Responsive design using Bootstrap 5
- Unit tests for core functionality

## Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript, jQuery, Bootstrap 5
- **Database:** SQLite (default, can be changed)
- **Testing:** Django TestCase

## Project Structure
IT/ # Project root
├── manage.py
├── IT/ # Project configuration
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── books/ # Main application
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── forms.py
│ ├── admin.py
│ ├── tests.py
│ ├── templates/books/ # HTML templates
│ └── static/books/ # CSS, JS files
├── requirements.txt
└── README.md


## Installation & Setup

1. **Clone or download the project**  
   Place the project folder at `D:\chengxu\IT` (or any location).

2. **Create a virtual environment (optional but recommended)**  
   Open a terminal in the project root and run:
   ```bash
   python -m venv venv
   # Activate it:
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
3.Install dependencies

pip install -r requirements.txt
4.Apply database migrations

python manage.py makemigrations books
python manage.py migrate
5.Create a superuser (for admin access)

python manage.py createsuperuser
Follow the prompts to set a username, email, and password.

6.Run the development server

python manage.py runserver

7.Access the application
Open your browser and go to http://127.0.0.1:8000/

Usage
Regular users: Register an account, browse books, borrow available books, and return them from "My Borrows".

Admin users: Log in to the admin panel at /admin or use the "Add Book" link in the navbar to manage books.

Running Tests
To execute the unit tests, run:
python manage.py test books

License
This project is created for educational purposes as part of a coursework assignment. Feel free to use and modify it for learning.

Acknowledgements
Built with Django

UI based on Bootstrap 5

Icons and design elements from course materials