from flask import request

def create_user():
    # Parse all arguments for validity
    args = request.get_json()

    # Make the insert query with parameters
    
    # Hash the password before inserting

    # Insert the user into the database

    # Return a message and the user id