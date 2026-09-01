from flask import Flask, render_template, request, redirect, url_for
from validator import validate_password

app = Flask(
    __name__,
    static_folder="Static",
    template_folder="templates"
)


# Home page
@app.route("/")
def home():
    return render_template("home.html")


# Security Checker
@app.route("/checker", methods=["GET", "POST"])
def checker():

    if request.method == "POST":

        password = request.form.get("password", "")

        # Validate password using validator.py
        is_valid, failed_rules = validate_password(password)

        # Send result to result page
        if is_valid:
            return redirect(url_for("result", status="valid"))
        else:
            return redirect(url_for("result", status="invalid"))

    return render_template("checker.html")


# Result page
@app.route("/result")
def result():

    status = request.args.get("status")

    if status == "valid":
        is_valid = True
    else:
        is_valid = False

    return render_template(
        "result.html",
        is_valid=is_valid
    )


if __name__ == "__main__":
    app.run(debug=True)