# Flask application instance
# Created: 01/03/2022
# Developer: Nitesh D
# Last Modified: 01/03/2022

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models, errors

#if __name__ == '__main__':
#    app.run(debug=True)
