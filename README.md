# 📝 Task Manager

A simple task management web application built with Django, featuring user authentication, task creation, editing, deletion, and status toggling.

## 🖼️ Screenshots

### Register Page
![Register Page](/screenshots/register.png)
*User registration form with email verification*

### Login Page
![Login Page](/screenshots/login.png)
*Secure login interface with Bootstrap styling*

### Task List
![Task List](/screenshots/task_list.png)
*Main dashboard showing tasks with completion status and action buttons*

### Create Task
![Create Task](/screenshots/create_task.png)
*Simple interface for adding new tasks*

### Delete Confirmation
![Delete Task](/screenshots/delete_task.png)
*Confirmation dialog before deleting a task*

## 🚀 Features
- ✅ User authentication (Register, Login, Logout)
- 📋 Create, update, delete tasks
- 🔄 Mark tasks as completed or pending
- 📄 Paginated task list
- 🎨 Bootstrap-styled UI

## 🛠 Installation

1. Clone the repository
```bash
git clone https://github.com/AbdulKareem-M/To-Do-App-Project.git
cd To-Do-App-Project
```

2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser (optional for admin access)
```bash
python manage.py createsuperuser
```

6. Start the development server
```bash
python manage.py runserver
```

7. Access the app
Open http://127.0.0.1:8000/ in your browser.

## 📌 URL Patterns

| URL | View | Description |
|-----|------|-------------|
| /register/ | RegistrationView | User registration |
| /login/ | CustomLoginView | User login |
| /logout/ | CustomLogoutView | User logout |
| /index/ | TaskListView | List all tasks |
| /new/ | TaskCreateView | Create a new task |
| /edit/<pk>/ | TaskUpdateView | Edit an existing task |
| /delete/<pk>/ | TaskDeleteView | Delete a task |
| /toggle/<pk>/ | TaskToggleView | Mark a task as completed or pending |

## 🎨 UI Overview
- **Login & Registration**: Secure authentication using Django's built-in forms.
- **Task List**: Displays tasks with completion status.
- **CRUD Operations**: Add, update, and delete tasks.
- **Pagination**: Large task lists are paginated for better navigation.

## 🛠 Tech Stack
- **Backend**: Django
- **Frontend**: HTML, Bootstrap
- **Database**: SQLite (default)

## 🤝 Contributing
1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Added feature"`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request
