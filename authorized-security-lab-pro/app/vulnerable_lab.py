from flask import Flask, request, render_template_string, session, redirect, url_for
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "TRAINING-ONLY-CHANGE-ME"
DB = Path(__file__).with_name("training.db")

def init_db():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, role TEXT)")
    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO users(username, role) VALUES (?, ?)",
            [("alice", "student"), ("admin", "admin")]
        )
    con.commit()
    con.close()

@app.route("/")
def index():
    return '''
    <h1>Authorized Security Training Lab</h1>
    <p>Intentionally vulnerable local training application.</p>
    <ul>
      <li><a href="/search?q=training">Search</a></li>
      <li><a href="/login">Training Login</a></li>
      <li><a href="/health">Health</a></li>
    </ul>
    '''

@app.route("/health")
def health():
    return {"status": "ok", "lab": "authorized", "scope": "LAB-01"}

@app.route("/search")
def search():
    # Intentional training weakness: reflected input.
    q = request.args.get("q", "")
    return render_template_string(
        "<h2>Search</h2><p>Query: " + q + "</p><p><a href='/'>Back</a></p>"
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    # Intentional training weakness: unsafe SQL construction.
    if request.method == "POST":
        username = request.form.get("username", "")
        query = "SELECT username, role FROM users WHERE username = '" + username + "'"
        con = sqlite3.connect(DB)
        row = con.execute(query).fetchone()
        con.close()

        if row:
            session["user"] = row[0]
            session["role"] = row[1]
            return redirect(url_for("profile"))

        return "<p>Login failed</p><a href='/login'>Back</a>", 401

    return '''
    <h2>Training Login</h2>
    <form method="post">
      <input name="username" placeholder="username">
      <button>Login</button>
    </form>
    <p>Training-only endpoint. Do not use real credentials.</p>
    '''

@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect(url_for("login"))
    return f"<h2>Profile</h2><p>User: {session['user']}</p><p>Role: {session['role']}</p>"

if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=8080, debug=False)
