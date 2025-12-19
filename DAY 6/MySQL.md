CREATE TABLE sensor_readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT,
    humidity FLOAT,
    timestamp DATETIME
);

INSERT INTO sensor_readings (temperature, humidity, timestamp)
VALUES (%s, %s, %s);

SELECT * FROM sensor_readings;

UPDATE sensor_readings
SET temperature = %s, humidity = %s
WHERE id = %s;

DELETE FROM sensor_readings
WHERE id = %s;

pip install mysql-connector-python
