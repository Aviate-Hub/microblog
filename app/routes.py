# Home page route
# Created: 01/03/2022
# Developer: Nitesh D
# Last Modified: 01/03/2022
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Nitesh'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Detroit'
		},
		{
			'author': {'username': 'Smith'},
			'body': 'The Matrix movie was so sucky!'
		},
		{
			'author': {'username': 'Dog'},
			'body': 'Give me some chickmen!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)
