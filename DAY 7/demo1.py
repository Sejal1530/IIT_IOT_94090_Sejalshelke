from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

#Database Connection
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "sensor_db",
    use_pure = True
)
#CREATE
@app.route('/add', methods=['POST'])
def add_reading():
    data = request.json
    temperature = data['temperature']
    humidity = data['humidity']
    time = datetime.now()

    db = mysql.connector.connect()
    cursor = db.cursor()

    query = """INSERT INTO sensor_readings
               (temperature, humidity, timestamp)
               VALUES (%s, %s, %s)"""
    cursor.execute(query, (temperature, humidity, time))
    db.commit()

    cursor.close()
    db.close()
    return jsonify({"message": "Sensor reading added successfully"})

#READ ALL 
@app.route('/readings', methods=['GET'])
def get_all_readings():
    db =mysql.connector.connect()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM sensor_readings")
    result = cursor.fetchall()

    cursor.close()
    db.close()
    return jsonify(result)

#READ BELOW THRESHOLD
@app.route('/threshold/<float:value>', methods=['GET'])
def get_below_threshold(value):
    db =mysql.connector.connect()
    cursor = db.cursor(dictionary=True)

    query = """SELECT * FROM sensor_readings
               WHERE temperature < %s"""
    cursor.execute(query, (value,))
    result = cursor.fetchall()

    cursor.close()
    db.close()
    return jsonify(result)

#UPDATE
@app.route('/update', methods=['PUT'])
def update_reading():
    data = request.json
    record_id = data['id']
    temperature = data['temperature']
    humidity = data['humidity']
    time = datetime.now()

    db = mysql.connector.connect()
    cursor = db.cursor()

    query = """UPDATE sensor_readings
               SET temperature=%s,
                   humidity=%s,
                   timestamp=%s
               WHERE id=%s"""
    cursor.execute(query, (temperature, humidity, time, record_id))
    db.commit()

    cursor.close()
    db.close()
    return jsonify({"message": "Record updated successfully"})

# DELETE
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_reading(id):
    db = mysql.connector.connect()
    cursor = db.cursor()

    query = "DELETE FROM sensor_readings WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()

    cursor.close()
    db.close()
    return jsonify({"message": "Record deleted successfully"})

# RUN SERVER 
if __name__ == '__main__':
    app.run(debug=True)
