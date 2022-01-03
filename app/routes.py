# Home page route
# Created: 01/03/2022
# Developer: Nitesh D
# Last Modified: 01/03/2022

from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Nitesh'}
	return render_template('index.html', title='Home', user=user)
