from flask import Flask, request, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

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

    validString = re.compile(r'^[\S]{3,20}$')
    validEmail = re.compile(r'^(?=\S{3,20}$)(?=[^@]*[@][^@]*$)(?=[^\.]*[\.][^\.]*$)')

    if not validString.match(userName):
        nameError = "User Name must be (3-20) characters with no spaces"
        validEntry = False

    if not validString.match(Pass):
        PassError = "Password must be (3-20) characters with no spaces"
        validEntry = False

    if rePass != Pass:
        rePassError = "Confirmation does not match"
        validEntry = False

    if len(email) == 0:
        pass
    elif not validEmail.match(email):
        emailError = "Not a vaild email"
        validEntry = False

    if validEntry == False:
        return render_template("index.html", title="Sign-up", userName=userName, nameError=nameError, PassError=PassError, rePassError=rePassError, email=email, emailError=emailError)
    else:
        return render_template("home.html", title="Welcome!", userName=userName)

if __name__ == "__main__":
    app.run()
