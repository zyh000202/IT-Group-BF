# IT Group BF

Library Management System – Coursework Project
Project Overview
This project is a web-based book management system. The system allows registered users to search, borrow and return books, and the administrator can manage the book catalog. The application is built using Django (back end) and Bootstrap 5 (front end) and deployed on Tencent Cloud Windows server.

Deployed Application: http://49.233.254.59:8000
Code Repository: (https://github.com/zyh000202/IT-Group-BF.git)

✅ Features Implemented (as per coursework requirements)
Category	Features
User Authentication	Register, login, logout (Django built-in auth). Access control for protected pages.
Database Interaction	Models for Book, Category, BorrowRecord. Full CRUD for books (admin only).
User Input	Search books by title/author; filter by category; borrow/return via AJAX.
Front-end Interactivity	AJAX borrow/return (no page reload); dynamic UI updates.
Responsive Design	Bootstrap 5 grid; adapts to mobile, tablet, desktop.
Accessibility	3+ improvements: ARIA labels for icon buttons; semantic HTML; color contrast (WCAG AA).
Sustainability	Lighthouse optimization: static file compression (WhiteNoise), removed unused CSS, image optimization.
Code Quality	Separation of concerns; reusable templates; unit tests for models and views.
Deployment	Live on Tencent Cloud (Windows Server) with public IP; accessible for marking.
🛠️ Technology Stack
Backend: Python 3.8, Django 4.2

Frontend: HTML5, CSS3, JavaScript, jQuery, Bootstrap 5

Database: SQLite (development), ready for PostgreSQL/MySQL

Static Files: WhiteNoise (production)

Deployment: Waitress WSGI server on Windows Server; Tencent Cloud security group configured.

🚀 Deployment & Access
The application is deployed on a Tencent Cloud Windows Server instance.

Public URL: http://49.233.254.59:8000

Admin Panel: http://49.233.254.59:8000/admin (use superuser credentials created during deployment)

Test User: You may create a new user via the registration page, or use the provided test account.

Note: The site uses HTTP (not HTTPS) for simplicity; all core features work correctly. Browser warnings about "not secure" can be ignored for marking purposes.

🧪 Running Tests
Unit tests cover core business logic and view responses. To run the test suite:

bash
python manage.py test books
Tests include:

Book.is_available() and BorrowRecord.is_overdue() methods

Borrow/return view permissions and responses

AJAX endpoint behavior

♿ Accessibility Improvements (3+ points)
Semantic HTML & Landmarks – <header>, <nav>, <main>, <footer> used correctly.

ARIA Labels – Added to icon-only buttons (navbar toggler, alert close button) for screen readers.

Color Contrast – Ensured text/background meet WCAG AA (4.5:1). Adjusted Bootstrap defaults where needed.

Keyboard Navigation – All interactive elements focusable and operable.

🌱 Sustainability Optimizations
Tool Used: Google Lighthouse

Pages Tested: Homepage and Book List page

Before: Performance score ~70, accessibility ~85

Actions Taken:

Enabled WhiteNoise for static file compression and caching.

Removed unused CSS (via manual audit).

Optimized external images (used placeholder with object-fit).

After: Performance ~98, accessibility ~100 (as of last test).
