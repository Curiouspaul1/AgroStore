from . import main
from flask import render_template,request,session,url_for,redirect

@main.route('/')
@main.route('/index')
def index():
   return render_template('index.html')

@main.route('/sign_up',methods=['GET','POST'])
def sign_up():
	return render_template('sign_in.html')