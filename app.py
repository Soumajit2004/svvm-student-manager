from flask import Flask
from flask import render_template
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return user_id


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
