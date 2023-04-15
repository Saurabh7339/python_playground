from flask import Flask
from flask import Blueprint

login_api  =  Blueprint("login_api",__name__)

@login_api.route("/",methods = ["OPTIONS","POST","GET"])
def login():
    return "<h3>welcome to the login page </h3>"