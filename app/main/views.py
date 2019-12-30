from . import main
from flask import render_template,request,session,url_for,redirect

@main.route('/')
@main.route('/index')
def index():
   return render_template('index.html')