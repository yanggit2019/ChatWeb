from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .models import get_user

bootstrap = Bootstrap()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your_secret_key"
    bootstrap.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"

    @login_manager.user_loader
    def load_user(user_id):
        return get_user(user_id)

    from .routes import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
