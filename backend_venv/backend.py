# Created by Lucas Videtto
# Backend connection for Course Compass

from flask import Flask, jsonify, request
from flask_cors import CORS
from mysql.connector import connect

app = Flask(__name__)
CORS(app)

@app.route('/api/courses', methods=['GET'])
def getCourses():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM courses')
    courses = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(courses)

@app.route('/api/courses', methods=['POST'])
def addCourse():
    newCourse = request.json
    ########
    ########
    ########
    return jsonify(newCourse), 201

def getConnection():
    connection = connect(
        host='####', # Replace with database credentials
        user='####',
        password='####',
        database='####'
    )
    return connection