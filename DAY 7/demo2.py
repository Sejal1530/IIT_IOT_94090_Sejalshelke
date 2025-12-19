from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
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
def add_record():
    data = request.json
    sensor_id = data['sensor_id']
    moisture = data['moisture_level']
    time = data['reading_time']

    db = mysql.connector.connect()
    cursor = db.cursor()
    query = """INSERT INTO sensor_readings 
               (sensor_id, moisture_level, reading_time)
               VALUES (%s, %s, %s)"""
    cursor.execute(query, (sensor_id, moisture, time))
    db.commit()

    cursor.close()
    db.close()
    return jsonify({"message": "Record inserted successfully"})

#READ ALL 
@app.route('/records', methods=['GET'])
def get_all_records():
    db = mysql.connector.connect()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sensor_readings")
    result = cursor.fetchall()

    cursor.close()
    db.close()
    return jsonify(result)

#READ BELOW THRESHOLD 
@app.route('/threshold/<float:value>', methods=['GET'])
def get_below_threshold(value):
    db = mysql.connector.connect()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM sensor_readings WHERE moisture_level < %s"
    cursor.execute(query, (value,))
    result = cursor.fetchall()

    cursor.close()
    db.close()
    return jsonify(result)

#UPDATE
@app.route('/update', methods=['PUT'])
def update_record():
    data = request.json
    sensor_id = data['sensor_id']
    moisture = data['moisture_level']
    time = data['reading_time']

    db = mysql.connector.connect()
    cursor = db.cursor()
    query = """UPDATE sensor_readings 
               SET moisture_level=%s, reading_time=%s
               WHERE sensor_id=%s"""
    cursor.execute(query, (moisture, time, sensor_id))
    db.commit()

    cursor.close()
    db.close()
    return jsonify({"message": "Record updated successfully"})

#DELETE 
@app.route('/delete/<int:sensor_id>', methods=['DELETE'])
def delete_record(sensor_id):
    db = mysql.connector.connect()
    cursor = db.cursor()
    query = "DELETE FROM sensor_readings WHERE sensor_id=%s"
    cursor.execute(query, (sensor_id,))
    db.commit()

    cursor.close()
    db.close()
    return jsonify({"message": "Record deleted successfully"})

#RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)
