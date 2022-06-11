from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap5 # Intancia de Bootstrap

bootstrap = Bootstrap5()

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)

    return app