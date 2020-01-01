from . import main
from flask import render_template,request,session,url_for,redirect

@main.route('/')
@main.route('/index')
def index():
	title = "Index"
	return render_template('index.html',title=title)

@main.route('/sign_up',methods=['GET','POST'])
def sign_up():
	title = "Create Account"
	return render_template('sign_in.html',title=title)