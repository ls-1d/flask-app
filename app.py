import sqlite3
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Football",
    "Soccer",
    "Frisbee",
]


# @app.route("/test")
# def text():
#     conn = sqlite3.connect("database.db")
#     c = conn.cursor()
#     tests = c.execute("SELECT * FROM registrants").fetchall()
#     conn.close()
#     return render_template("test.html", tests=tests)


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/delete/<int:user_id>", methods=["GET", "POST"])
def delete(user_id):

    if user_id:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("DELETE FROM registrants WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()

    return redirect("/registrants")


@app.route("/register", methods=["POST"])
def register():

    # validating name
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name:
        return render_template("error.html", message="Missing Name")
    if not sport:
        return render_template("error.html", message="Missing Sport")

    # remember registrant
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", (name, sport))
    conn.commit()
    conn.close()

    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    REGISTRANTS = c.execute("SELECT * FROM registrants").fetchall()
    conn.close()

    return render_template("registrants.html", registrants=REGISTRANTS)


if __name__ == "__main__":
    app.run(debug=True)
    app.run()
