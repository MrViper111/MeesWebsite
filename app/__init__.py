from flask import Flask

from app.views import views


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "f4nf4f3n48904fkkjfkshf2f298323-232-fioefjeio"

    app.register_blueprint(views)

    return app
