# Home page route
# Created: 01/03/2022
# Developer: Nitesh D
# Last Modified: 01/03/2022
from flask import render_template, flash, redirect, url_for
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


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
		form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)
