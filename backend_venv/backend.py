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

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['Email']
    password = data['Passwd']
    
    connection = getConnection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tblUser WHERE Email = %s", (email, ))
    user = cursor.fetchone()
    
    if user and hashlib.sha256(password.encode()).hexdigest() == user['Passwd']:
        token = hashlib.sha256(os.urandom(64)).hexdigest()
        expiration = datetime.now() + timedelta(hours = 48)
        
        # Store token and token expiration in database (not necessary for demo)
        cursor.close()
        connection.close()
        return  jsonify({"message": "Login successful", "user": user, "token": token, "expires": expiration.isoformat()}), 200
    else:
        cursor.close()
        connection.close()
        return jsonify({"message": "Incorrect username or password"}), 401

@app.route('/api/courses', methods=['GET'])
def getCourses():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM courses')
    courses = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(courses)

def getConnection():
    connection = connect(
        host='####', # Replace with database credentials
        user='####',
        password='####',
        database='####'
    )
    return connection

#if __name__ == '__main--':
    #app.run(debug=True)