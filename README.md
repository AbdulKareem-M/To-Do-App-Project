📝 Task Manager
A simple task management web application built with Django, featuring user authentication, task creation, editing, deletion, and status toggling.

🚀 Features
✅ User authentication (Register, Login, Logout)
📋 Create, update, delete tasks
🔄 Mark tasks as completed or pending
📄 Paginated task list
🎨 Bootstrap-styled UI


🛠 Installation
Clone the repository
git clone https://github.com/AbdulKareem-M/To-Do-App-Project.git
cd To-Do-App-Project


Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies
pip install -r requirements.txt

Run migrations
python manage.py makemigrations
python manage.py migrate


Create a superuser (optional for admin access)
python manage.py createsuperuser


Start the development server
python manage.py runserver


Access the app
Open http://127.0.0.1:8000/ in your browser.

📌 URL Patterns
URL	View	Description
/register/	RegistrationView	User registration
/login/	CustomLoginView	User login
/logout/	CustomLogoutView	User logout
/index/	TaskListView	List all tasks
/new/	TaskCreateView	Create a new task
/edit/<pk>/	TaskUpdateView	Edit an existing task
/delete/<pk>/	TaskDeleteView	Delete a task
/toggle/<pk>/	TaskToggleView	Mark a task as completed or pending


🎨 UI Overview
Login & Registration: Secure authentication using Django's built-in forms.
Task List: Displays tasks with completion status.
CRUD Operations: Add, update, and delete tasks.
Pagination: Large task lists are paginated for better navigation.

🛠 Tech Stack
Backend: Django
Frontend: HTML, Bootstrap
Database: SQLite (default)

🤝 Contributing
Fork the repository
Create a new branch: git checkout -b feature-name
Commit changes: git commit -m "Added feature"
Push to branch: git push origin feature-name
Submit a pull request
