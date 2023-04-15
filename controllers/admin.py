from crypt import methods
from flask import Flask
from flask import Blueprint

admin_api  = Blueprint("admin_api",__name__)

@admin_api.route("/", methods =["OPTIONS","GET"])
def home():
    return "hey"

