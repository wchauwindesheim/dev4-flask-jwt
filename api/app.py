from flask import Flask
from flask_cors import CORS
<<<<<<< HEAD
from db import create_database
=======
from db import DB
from resources.user import create_user
from security import login, me
>>>>>>> uitwerking

# Create a new Flask application
app = Flask(__name__)
app.debug = True

# Enable cors on the server
CORS(app)

# Register the JWT manager

# ============================ Routes ============================

# JWT routes


# Start app
if __name__ == '__main__':
    DB.create()
    app.run()