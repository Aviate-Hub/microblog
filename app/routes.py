# Home page route
# Created: 01/03/2022
# Developer: Nitesh D
# Last Modified: 01/03/2022

from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Nitesh'}
	return '''
	<html>
		<head>
			<title>Home page - Flask Microblog</title>
		</head>
		<body>
			<h1>Hello, ''' + user['username'] + '''!</h1>
		</body>
	</html>
	'''
