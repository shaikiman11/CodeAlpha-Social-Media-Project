# 🌐 ConnectHub — Social Media Platform

ConnectHub is a mini social media web application developed as part of my **CodeAlpha Full Stack Development Internship**.

The application allows users to register, log in, create posts, interact with posts, comment, view profiles, and follow or unfollow other users.

---

## 🚀 Features

### 👤 User Authentication
- User registration
- User login
- User logout
- Authentication-protected features

### 📝 Posts
- Create posts
- View latest posts
- View posts from individual users
- Display post creation time

### ❤️ Like System
- Like posts
- Unlike posts
- Display like count

### 💬 Comments
- Add comments to posts
- Display comments with usernames

### 👥 Follow System
- Follow users
- Unfollow users
- Display followers count
- Display following count
- Display current following status

### 👤 User Profiles
- View user profiles
- Display username
- Display number of posts
- Display followers
- Display following
- View user's posts

### 🎨 User Interface
- Clean and modern interface
- Responsive design
- Navigation bar
- Styled post cards
- Mobile-friendly layout

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Django

### Database
- SQLite

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```text
CodeAlpha-Social-Media-Project/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── social/
│   ├── migrations/
│   ├── static/
│   │   └── social/
│   │       └── style.css
│   │
│   ├── templates/
│   │   └── social/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       └── profile.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── .gitignore
└── README.md
```

🗄️ Database Models

The application uses Django models to manage social media data.

Post

Stores:

User
Post content
Creation time

Comment

Stores:

Post
User
Comment content
Creation time

Like

Stores:

Post
User

A user can like a particular post only once.

Follow

Stores:

Follower
Following

This model handles the follow and unfollow functionality.

User

Django's built-in authentication system is used for managing users.

⚙️ Installation and Setup

1. Clone the repository
   
git clone https://github.com/shaikiman11/CodeAlpha-Social-Media-Project.git

2. Navigate into the project.
    
cd CodeAlpha-Social-Media-Project

3. Create a virtual environment
 
python -m venv venv

4. Activate the virtual environment

Windows
venv\Scripts\activate

5. Install Django
   
pip install django

6. Apply database migrations
   
python manage.py migrate

7. Start the development server
   
python manage.py runserver

8. Open the application
   
http://127.0.0.1:8000/

🔐 Authentication Flow

Users can create an account using the registration page.
Registered users can log in.
Authenticated users can create posts.
Users can like and comment on posts.
Users can view other user profiles.
Users can follow or unfollow other users.
Users can log out.

📱 Main Application Pages

🏠 Home Feed

Displays the latest posts and allows authenticated users to create posts, like posts and add comments.

👤 Profile

Displays a user's posts, followers, following count and profile information.

🔐 Login

Allows registered users to access their account.

📝 Register

Allows new users to create an account.

🎯 CodeAlpha Internship Task

Internship: CodeAlpha Full Stack Development Internship

Task: Task 2 — Social Media Platform

The project implements the required social media functionality including:

User profiles
Posts
Comments
Like system
Follow system
User authentication
Database integration

👨‍💻 Developer

Shaik Iman

GitHub: https://github.com/shaikiman11

📄 License

This project was developed for educational
