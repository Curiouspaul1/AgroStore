from flask import Blueprint

main = Blueprint('main',__name__,static_folder='',template_folder='templates')

from . import views,errors

