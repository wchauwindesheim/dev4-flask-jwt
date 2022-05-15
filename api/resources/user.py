from flask import request, jsonify
from flask_bcrypt import generate_password_hash
from db import DB

def create_user():
    try:
        # Parse all arguments for validity
        args = request.get_json()
        print(args)
        # Make the insert query with parameters
        query = '''
        insert into 'users' values (:email, :password, :firstname, :lastname)
        '''
        # Hash the password before inserting
        args['password'] = generate_password_hash(args['password'])

        # Insert the user into the database
        DB.insert(query, args)
        # Return a message and the user id
        return {'message': 'success', 'id': id}, 201    
    except BaseException as error:
        print('in exception handler')
        return {'error': f'{error}'}