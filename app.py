from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# Temporary storage
entries = []


# ===================== HOME PAGE =====================

@app.route("/")
def home():
    return render_template("index.html")



# ===================== ADD SKILL =====================

@app.route("/add", methods=["GET", "POST"])
def add_entry():

    if request.method == "POST":

        entry = {

            "skill": request.form["skill"],
            "category": request.form["category"],
            "level": request.form["level"],
            "progress": request.form["progress"],
            "study_time": request.form["study_time"],
            "learning": request.form["learning"],
            "confusion": request.form["confusion"]

        }

        entries.append(entry)

        return redirect("/entries")


    return render_template("add_entry.html")



# ===================== SKILL LIST =====================

@app.route("/entries")
def journal():

    return render_template(
        "entries.html",
        entries=entries
    )



# ===================== EDIT SKILL =====================

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_entry(index):

    if request.method == "POST":

        entries[index] = {

            "skill": request.form["skill"],
            "category": request.form["category"],
            "level": request.form["level"],
            "progress": request.form["progress"],
            "study_time": request.form["study_time"],
            "learning": request.form["learning"],
            "confusion": request.form["confusion"]

        }

        return redirect("/entries")


    return render_template(
        "edit_entry.html",
        entry=entries[index],
        index=index
    )



# ===================== DELETE SKILL =====================

@app.route("/delete/<int:index>")
def delete_entry(index):

    entries.pop(index)

    return redirect("/entries")



# ===================== ABOUT PAGE =====================

@app.route("/about")
def about():

    return render_template("about.html")



# ===================== RUN =====================

if __name__ == "__main__":

    app.run(debug=True)