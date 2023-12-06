# Created by Lucas Videtto
# Backend connection for Course Compass

from flask import Flask, jsonify, request
from flask_cors import CORS
from mysql.connector import connect, Error
from datetime import datetime, timedelta
import hashlib
import os

app = Flask(__name__)
CORS(app)

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