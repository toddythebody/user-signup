from flask import Flask, redirect, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/', methods=['POST'])
def index():
    userName = request.form("userName")
    nameError = ''
    Pass = request.form("Pass")
    PassError = ''

@app.route('/home')
def home():
    return render_template("home.html", userName=userName)
