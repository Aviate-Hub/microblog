# Flask application instance
# Created: 01/03/2022
# Developer: Nitesh D
# Last Modified: 01/03/2022

from flask import Flask

app = Flask(__name__)

from app import routes

#if __name__ == '__main__':
#    app.run(debug=True)
