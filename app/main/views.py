from . import main
from flask import render_template,request,session,url_for,redirect

@main.route('/')
@main.route('/index')
def index():
    render_template('index.html')