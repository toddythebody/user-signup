from flask import Flask, redirect, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

def validate(text):
    if len(text) < 3 or len(text) > 20:
        return False
    for i in text:
        if i == ' ':
            return False
    return True

@app.route('/')
def displayIndex():
    return render_template('index.html', title="Sign-up")

@app.route('/', methods=['POST'])
def index():
    userName = request.form["userName"]
    Pass = request.form["Pass"]
    rePass = request.form["rePass"]
    email = request.form["email"]
    nameError = ''
    PassError = ''
    rePassError = ''
    emailError = ''
    validEntry = True

    if validate(userName) == False:
        nameError = "User Name must be (3-20) characters with no spaces"
        validEntry = False

    if validate(Pass) == False:
        PassError = "Password must be (3-20) characters with no spaces"
        validEntry = False

    if rePass != Pass:
        rePassError = "Confirmation does not match"
        validEntry = False

    if len(email) == 0:
        pass
    elif validate(email) == False:
        emailError = "Email must be (3-20) characters with no spaces"
        validEntry = False
    elif "@" not in email or "." not in email:
        emailError = "Not a vaild email"
        validEntry = False

    if validEntry == False:
        return render_template("index.html", title="Sign-up", userName=userName, nameError=nameError, PassError=PassError, rePassError=rePassError, email=email, emailError=emailError)
    else:
        return render_template("home.html", title="Welcome!", userName=userName)

if __name__ == "__main__":
    app.run()
