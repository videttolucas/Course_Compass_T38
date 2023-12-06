# Created by Lucas Videtto
# Backend connection for Course Compass

from flask import Flask, jsonify, request, session
from flask_cors import CORS
from mysql.connector import connect, Error
from datetime import datetime, timedelta
import hashlib
import os

app = Flask(__name__)
app.secret_key = '12345'
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']
    
    demo_email = '425demo@example.com' # For demo showcase / plan b
    demo_pw = 'Password1!'
    
    if email == demo_email and password == demo_pw:
        print("User logged in and session started") # Print check for testing purposes
        session['user_email'] = email
        return jsonify({"message": "Demo login successful"}), 200
    
    connection = connectToDB()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM cs425.tblUser WHERE Email = %s", (email,))
            user = cursor.fetchone()
            if user and user['Passwd'] == password:
                session['user_email'] = email
                return jsonify({"message": "Login successful"}), 200
            else:
                return jsonify({"error": "Invalid email or password"}), 401
        except Error as err:
            print("Error while authenticating user", err)
            return jsonify({"error": str(err)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Database connection failed"}), 500
    
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    firstname = data['firstname']
    lastname = data['lastname']
    email = data['email']
    password = data['password']
    majorID = data['majorID']
    
    connection = connectToDB()
    if connection is not None:
        cursor = connection.cursor()
        try:
            insertQuery = """INSERT INTO cs425.tblUser (Fname, Lname, Email, Passwd, majorID) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(insertQuery, (firstname, lastname, email, password, majorID))
            connection.commit()
            return jsonify({"message": "Signup successful"}), 200
        except Error as err:
            print("Error while inserting data into database", err)
            return jsonify({"error": str(err)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Database connection failed"}), 500

def connectToDB():
    try:
        connection = connect(
            host=os.getenv('DB_HOST', 'default_host'),
            database=os.getenv('DB_NAME', 'default_db_name'),
            user=os.getenv('DB_USER', 'default_user'),
            password=os.getenv('DB_PASSWORD', 'default_password')
        )
        return connection
    except Error as err:
        print("Error while connecting to database", err)
        return None

app.run(debug=True)