from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Home page (custom URL)
@app.route("/nextgen")
def home():
    return render_template("home.html")

# Signup page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        domain = request.form["domain"]

        # Generate unique code
        code = "NGI-" + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )

        return render_template(
            "success.html",
            code=code,
            domain=domain
        )

    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)