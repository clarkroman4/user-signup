from flask import Flask, request, redirect, render_template
import html


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template("signup_form.html")

@app.route("/", methods=["POST"])


def validation ():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    if len(username)< 3 or len(username)>20 or ' ' in username:
        username_error = "Please enter a username with no spaces, between 3 and 20 characters."
        return render_template("signup_form.html", username= username, username_error = username_error)
    
    if len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = "Please enter a password with no spaces, between 3 and 20 characters."
        return render_template("signup_form.html", username = username, email = email, password_error = password_error)
    if password != verify_password:
        verify_error = "Both 'password' and 'verify password' must match."
        return render_template("signup_form.html", username = username, email = email, verify_error = verify_error)
    if email != '':
        if email.count("@") != 1 or email.count(".") != 1 or ' ' in email or len(email) < 3 or len(email) > 20:
            email_error = "Please enter a valid email."
            return render_template("signup_form.html", username = username, email= email, email_error = email_error)
        else:
            return redirect ("/welcome?username={0}".format(username))
    else:
        return redirect("/welcome?username={0}".format(username))


@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("signup_confirm.html", username = username)


app.run()