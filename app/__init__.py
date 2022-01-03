# Flask application instance
# Created: 01/03/2022
# Developer: Nitesh D
# Last Modified: 01/03/2022

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

#if __name__ == '__main__':
#    app.run(debug=True)
