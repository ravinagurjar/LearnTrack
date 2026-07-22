from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from models import db, Skill


# ======================================================
# Flask Configuration
# ======================================================

app = Flask(__name__)

app.config["SECRET_KEY"] = "learntrack_secret_key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///learntrack.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# ======================================================
# Initialize Database
# ======================================================

db.init_app(app)

with app.app_context():
    db.create_all()


# ======================================================
# Simple Login Credentials
# Demonstration credentials used.
# ======================================================

USERNAME = "admin"
PASSWORD = "admin123"


# ======================================================
# Login Required Helper
# ======================================================

def is_logged_in():
    return session.get("logged_in", False)
# ======================================================
# Login
# ======================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    # If already logged in, go to Home
    if is_logged_in():
        return redirect(url_for("home"))

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:

            session["logged_in"] = True

            flash("Login successful!", "success")

            return redirect(url_for("home"))

        else:

            flash("Invalid username or password.", "error")

    return render_template("login.html")


# ======================================================
# Logout
# ======================================================

@app.route("/logout")
def logout():

    session.clear()

    flash("You have been logged out.", "success")

    return redirect(url_for("login"))


# ======================================================
# Home Dashboard
# ======================================================

@app.route("/")
def home():

    if not is_logged_in():
        return redirect(url_for("login"))

    total_entries = Skill.query.count()

    total_study_time = db.session.query(
        db.func.sum(Skill.study_time)
    ).scalar()

    if total_study_time is None:
        total_study_time = 0

    average_progress = db.session.query(
        db.func.avg(Skill.progress)
    ).scalar()

    if average_progress is None:
        average_progress = 0

    average_progress = round(average_progress)

    recent_entries = (
        Skill.query
        .order_by(Skill.id.desc())
        .limit(5)
        .all()
    )

    return render_template(
        "index.html",
        total_entries=total_entries,
        total_study_time=total_study_time,
        average_progress=average_progress,
        recent_entries=recent_entries
    )
# ======================================================
# Add New Entry
# ======================================================

@app.route("/add", methods=["GET", "POST"])
def add_entry():

    if not is_logged_in():
        return redirect(url_for("login"))

    if request.method == "POST":

        new_entry = Skill(

            skill=request.form["skill"],

            category=request.form["category"],

            level=request.form["level"],

            progress=int(request.form["progress"]),

            study_time=int(request.form["study_time"]),

            learning=request.form["learning"],

            confusion=request.form["confusion"]

        )

        db.session.add(new_entry)

        db.session.commit()

        flash("Learning entry added successfully!", "success")

        return redirect(url_for("view_entries"))

    return render_template("addentries.html")


# ======================================================
# View All Entries
# ======================================================

@app.route("/view-entries")
def view_entries():

    if not is_logged_in():
        return redirect(url_for("login"))

    entries = Skill.query.order_by(Skill.id.desc()).all()

    return render_template(

        "view_entries.html",

        entries=entries

    )
# ======================================================
# Edit Entry
# ======================================================

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_entry(id):

    if not is_logged_in():
        return redirect(url_for("login"))

    entry = Skill.query.get_or_404(id)

    if request.method == "POST":

        entry.skill = request.form["skill"]

        entry.category = request.form["category"]

        entry.level = request.form["level"]

        entry.progress = int(request.form["progress"])

        entry.study_time = int(request.form["study_time"])

        entry.learning = request.form["learning"]

        entry.confusion = request.form["confusion"]

        db.session.commit()

        flash("Learning entry updated successfully!", "success")

        return redirect(url_for("view_entries"))

    return render_template(

    "edit_entries.html",

    entry=entry

)


# ======================================================
# Delete Entry
# ======================================================

@app.route("/delete/<int:id>")
def delete_entry(id):

    if not is_logged_in():
        return redirect(url_for("login"))

    entry = Skill.query.get_or_404(id)

    db.session.delete(entry)

    db.session.commit()

    flash("Learning entry deleted successfully!", "success")

    return redirect(url_for("view_entries"))
# ======================================================
# Search Entries
# ======================================================

@app.route("/search", methods=["GET"])
def search():

    if not is_logged_in():
        return redirect(url_for("login"))

    keyword = request.args.get("keyword", "").strip()

    category = request.args.get("category", "").strip()

    query = Skill.query

    if keyword:
        query = query.filter(
            Skill.skill.ilike(f"%{keyword}%")
        )

    if category:
        query = query.filter(
            Skill.category == category
        )

    entries = query.order_by(Skill.id.desc()).all()

    return render_template(

        "search.html",

        entries=entries,

        keyword=keyword,

        category=category

    )


# ======================================================
# About Page
# ======================================================

@app.route("/about")
def about():

    if not is_logged_in():
        return redirect(url_for("login"))

    return render_template("about.html")


# ======================================================
# Error Pages (Optional)
# ======================================================

@app.errorhandler(404)
def page_not_found(error):

    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):

    db.session.rollback()

    return render_template("500.html"), 500


# ======================================================
# Run Application
# ======================================================

if __name__ == "__main__":

    app.run(

        debug=True

    )