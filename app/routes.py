from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, users
from .forms import RegistrationForm, LoginForm

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username in [user.username for user in users.values()]:
            flash("Username already exists", "danger")
            return redirect(url_for("main.register"))
        user_id = str(len(users) + 1)
        new_user = User(user_id, username, password)
        users[user_id] = new_user
        flash("Registration successful", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = next(
            (
                u
                for u in users.values()
                if u.username == username and u.check_password(password)
            ),
            None,
        )
        if user:
            login_user(user)
            return redirect(url_for("main.chat"))  # 登录成功后重定向到聊天页面
        flash("Invalid username or password", "danger")
    return render_template("login.html", form=form)


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@main.route("/dashboard")
@login_required
def dashboard():
    return f"Hello, {current_user.username}!"


@main.route("/chat")
@login_required  # 确保用户登录后才能访问聊天页面
def chat():
    return render_template("chat.html")
