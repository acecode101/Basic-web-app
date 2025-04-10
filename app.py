import os
from flask import Flask, request, redirect, session, render_template_string

app = Flask(__name__)
app.secret_key = "secret"  # Needed for session

users = {"admin": "pass123"}  # Simple user store

login_page = '''
<form method="POST">
  Username: <input name="username"><br>
  Password: <input name="password" type="password"><br>
  <input type="submit" value="Login">
</form>
'''

@app.route("/")
def home():
    if "user" in session:
        return f"Welcome {session['user']}!"
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u, p = request.form["username"], request.form["password"]
        if u in users and users[u] == p:
            session["user"] = u
            return redirect("/")
    return render_template_string(login_page)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
