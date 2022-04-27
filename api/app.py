from flask import Flask
from flask_cors import CORS
from db import create_database

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
    create_database()
    app.run()