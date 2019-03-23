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

@app.route('/', methods=['POST'])
def index():
    userName = request.form("userName")
    nameError = ''
    Pass = request.form("Pass")
    PassError = ''
    rePass = request.form("rePass")
    rePassError = ''
    email = request.form("email")
    emailError = ''

    if validate(userName) == False:
        nameError = "User Name must be (3-20) characters with no spaces"
        Pass = ''
        rePass = ''

    if validate(Pass) == False:
        PassError = "Password must be (3-20) characters with no spaces"
        Pass = ''
        rePass = ''

    if rePass != Pass:
        rePassError = "Confirmation does not match"
        Pass = ''
        rePass = ''

    if len(email) == 0:
        pass
    elif validate(email) == False:
        emailError = "Email must be (3-20) characters with no spaces"
        Pass = ''
        rePass = ''

    if "@" not in email and "." not in email:
        emailError = "Not a vaild email"
        Pass = ''
        rePass = ''

    if Pass == '' and rePass == '':
        return render_template("/", userName=userName, nameError=nameError, PassError=PassError, rePassError=rePassError, email=email, emailError=emailError)
    else:
        return render_template("home.html", userName=userName)

@app.route('/home')
def home():
    return render_template("home.html", userName=userName)
