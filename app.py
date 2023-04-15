from crypt import methods
from flask import Flask
from kernel import add_blueprints


def create_app():
    app = Flask(__name__)
    add_blueprints(app)
    @app.route("/",methods=["GET"])
    def home():
        return "<h1>welcome to home screen</h1>"
    app.run(host="0.0.0.0", port=3000,debug=True)


if __name__ == "__main__":
    create_app()