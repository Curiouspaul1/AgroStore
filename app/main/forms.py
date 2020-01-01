from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import DataRequired
from .models import Space_cat

class StoreSignUp(FlaskForm):
	#personal details
	name = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	tel = StringField('Telephone',validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired()])
	home_address = StringField('Home address',validators=[DataRequired()])
	farm_address = StringField('Farm address',validators=[DataRequired()])

	# farmSpace details
	store_name = StringField('Store name',validators=[DataRequired()])
	description = TextAreaField('description',validators=[DataRequired()])
	store_tel = StringField('Store Tel',validators=[DataRequired()])
	store_email = StringField('Store Email',validators=[DataRequired()])
	category = SelectField('category')
	submit = SubmitField('Sign Up')

def __init__(self, *args, **kwargs):
	super(StoreSignUp, self).__init__(*args, **kwargs)
	self.category.choices = [(space_cat.id, space_cat.name) for cat in Space_cat.query.order_by(Space_cat.name).all()]

class SignUp(FlaskForm):
	#personal details
	name = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	tel = StringField('Telephone',validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired()])
	address = StringField('Home address',validators=[DataRequired()])
