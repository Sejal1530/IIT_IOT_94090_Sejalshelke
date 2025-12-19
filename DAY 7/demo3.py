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

#UPDATE SENSOR DATA 
@app.route('/update', methods=['POST'])
def update_status():
    data = request.json

    light = data['light_status']     # ON / OFF
    fan = data['fan_status']         # ON / OFF
    temp = data['temperature']       # float
    time = datetime.now()

    db = mysql.connector.connect()
    cursor = db.cursor()

    query = """INSERT INTO home_status
               (light_status, fan_status, temperature, updated_time)
               VALUES (%s, %s, %s, %s)"""

    cursor.execute(query, (light, fan, temp, time))
    db.commit()

    cursor.close()
    db.close()

    return jsonify({"message": "Home status updated successfully"})

#SHOW CURRENT STATUS
@app.route('/status', methods=['GET'])
def show_status():
    db = mysql.connector.connect()
    cursor = db.cursor(dictionary=True)

    query = """SELECT light_status, fan_status, temperature, updated_time
               FROM home_status
               ORDER BY id DESC
               LIMIT 1"""

    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    db.close()

    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "No data available"})

#RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)
