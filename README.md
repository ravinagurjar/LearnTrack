# LearnTrack

LearnTrack is a web-based learning tracker developed using **Python**, **Flask**, **SQLite**, **HTML**, and **CSS**. It helps users organize their learning journey by recording skills, tracking progress, managing study time, and maintaining personal learning notes in one place.

This project was developed as part of a **Second-Year B.Tech (Computer Science Engineering)** curriculum to gain practical experience with Flask web development, SQLAlchemy, template rendering, session management, and CRUD operations.

---

## Project Overview

Learning multiple technologies often makes it difficult to remember completed topics, monitor progress, and identify concepts that need revision. LearnTrack solves this problem by providing a simple and organized platform where users can add, update, search, and manage their learning records efficiently.

The project focuses on clean code, beginner-friendly implementation, and practical use of Flask with a relational database.

---

## Features

- Secure session-based login
- Dashboard with learning statistics
- Add new learning entries
- View all saved entries
- Edit existing entries
- Delete learning entries
- Search entries by keyword and category
- Flash messages for user feedback
- Custom 404 and 500 error pages
- Responsive user interface

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

```text
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

### Skill Model

| Field | Type |
|--------|------|
| id | Integer |
| skill | String |
| category | String |
| level | String |
| progress | Integer |
| study_time | Integer |
| learning | Text |
| confusion | Text |

---

## Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/ravinagurjar/LearnTrack.git
```

### 2. Navigate to the project directory

```bash
cd LearnTrack
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

### 5. Open your browser

```
http://127.0.0.1:5000
```

---

## Demo Login Credentials

Use the following default administrator account to explore the application.

| Username | Password |
|----------|----------|
| `admin` | `admin123` |

> **Note:** These credentials are provided only for demonstration purposes. In a production application, user authentication should use securely stored and hashed passwords.

---

## Future Improvements

Future enhancements may include:

- User registration
- Multiple user accounts
- Password hashing
- Charts and analytics dashboard
- Export entries as PDF or Excel
- File attachments
- Dark/Light mode
- Email reminders
- Learning streak tracking

---

## Author

**Ravina Gurjar**

Second Year B.Tech (Computer Science Engineering)

---

## License

This project is intended for educational and learning purposes.