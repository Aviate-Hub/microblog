# Main application instance
# Created: 01/03/2022
# Developer: Nitesh D
# Last Modified: 01/03/2022

from app import app
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
