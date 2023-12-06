# Created by Lucas Videtto
# Backend connection for Course Compass

from flask import Flask, jsonify, request
from flask_cors import CORS
from mysql.connector import connect
from datetime import datetime, timedelta
import hashlib
import os

app = Flask(__name__)
CORS(app)

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     email = data['Email']
#     password = data['Passwd']
    
#     connection = getConnection()
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM tblUser WHERE Email = %s", (email, ))
#     user = cursor.fetchone()
    
#     if user and hashlib.sha256(password.encode()).hexdigest() == user['Passwd']:
#         token = hashlib.sha256(os.urandom(64)).hexdigest()
#         expiration = datetime.now() + timedelta(hours = 48)
        
#         # Store token and token expiration in database (not necessary for demo)
#         cursor.close()
#         connection.close()
#         return  jsonify({"message": "Login successful", "user": user, "token": token, "expires": expiration.isoformat()}), 200
#     else:
#         cursor.close()
#         connection.close()
#         return jsonify({"message": "Incorrect username or password"}), 401
    
# @app.route('/signup', method=['POST'])
# def signup():
#     data = request.json
#     firstName = data['Fname']
#     lastName = data['Lname']
#     email = data['Email']
#     pw = hashlib.sha256(data['Passwd'].encode()).hexdigest()
#     majorId = data['majorID']
    
#     connection = getConnection()
#     cursor = connection.cursor()
    
#     cursor.execute("SELECT * FROM tblUser WHERE Email = %s", (email,))
#     if cursor.fetchone():
#         return jsonify({"message": "Email already registered"}), 409
    
#     cursor.execute(
#         "INSERT INTO tblUser (Fname, Lname, Email, Passwd, majorID) VALUES (%s, %s, %s, %s, %s)",
#         (firstName, lastName, email, pw, majorId))
    
#     connection.commit()
#     cursor.close()
#     connection.close()
    
#     return jsonify({"message": "Successfully created new account"}), 201

def getConnection():
    connection = connect(
        host='aws.connect.psdb.cloud',
        user='kvq86gq6g04wsq6lz3vi',
        password='pscale_pw_mJzru53sidNF7YadEPHFKE0ATfvcJK9EFgBQxy7JCCa',
        database='cs425'
    )
    
    if connection:
        print('Connection successful')
        
    return connection

getConnection()

if __name__ == '__main--':
    app.run(debug=True)