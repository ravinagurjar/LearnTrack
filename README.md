# LearnTrack

LearnTrack is a web-based learning tracker developed using **Python Flask**, **SQLite**, **HTML**, and **CSS**. The project allows users to record their daily learning activities, monitor progress, and maintain personal learning notes in one place.

This project was developed as a second-year B.Tech (Computer Science Engineering) project to understand the fundamentals of Flask web development, SQLAlchemy, template rendering, and CRUD operations.

---

## Project Overview

While learning different technologies, it becomes difficult to remember what has been studied, how much progress has been made, and which topics still need revision. LearnTrack solves this problem by providing a simple platform where learning entries can be added, updated, searched, and managed efficiently.

The project focuses on clean code, beginner-friendly implementation, and practical usage of Flask with a relational database.

---

## Features

- User login using session-based authentication
- Dashboard showing learning statistics
- Add new learning entries
- View all saved entries
- Edit existing entries
- Delete entries
- Search entries by keyword and category
- Flash messages for user feedback
- Custom 404 and 500 error pages
- Responsive interface for different screen sizes

---

## Technologies Used

### Backend

- Python
- Flask
- Flask-SQLAlchemy
- SQLite

### Frontend

- HTML5
- CSS3
- Jinja2 Templates

---

## Project Structure

```
LearnTrack/
│
├── app.py
├── models.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── index.html
│   ├── addentries.html
│   ├── edit_entries.html
│   ├── view_entries.html
│   ├── search.html
│   ├── about.html
│   ├── 404.html
│   └── 500.html
│
└── instance/
    └── learntrack.db
```

---

## Database

The project uses **SQLite** with **Flask-SQLAlchemy**.

Current model:

| Field | Type |
|-------|------|
| id | Integer |
| skill | String |
| category | String |
| level | String |
| progress | Integer |
| study_time | Integer |
| learning | Text |
| confusion | Text |

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Open the project folder

```bash
cd LearnTrack
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## Login Credentials

```
Username : admin
Password : admin123
```

---

## Screenshots

You can add screenshots here after uploading the project to GitHub.

Suggested screenshots:

- Login Page
- Dashboard
- Add Entry
- View Entries
- Search Page
- About Page

---

## What I Learned

While building this project, I gained practical experience with:

- Flask routing
- Jinja template inheritance
- Session management
- SQLAlchemy ORM
- SQLite database integration
- CRUD operations
- Form handling
- Flash messages
- Error handling
- Responsive web design

---

## Future Improvements

Some features that can be added in future versions are:

- User registration
- Multiple user accounts
- Password hashing
- Charts and analytics
- Export entries as PDF or Excel
- File attachments
- Dark/Light theme
- Email reminders
- Learning streak tracking

---

## Author

**Ravina Gurjar**

Second Year B.Tech (Computer Science Engineering)

---

## Note

This project was created for learning purposes as part of a college web development project. The main objective was to understand Flask application development and database integration by building a complete CRUD-based web application.