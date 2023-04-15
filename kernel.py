from flask import Flask
from flask import Blueprint
from controllers.admin import admin_api
from controllers.login import login_api

def add_blueprints(app):
    app.register_blueprint(admin_api, url_prefix="/admin")
    app.register_blueprint(login_api,url_prefix= "/login")
    return app