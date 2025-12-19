INSERT_QUERY = """
INSERT INTO sensor_data (sensor_id, moisture_level, date_time)
VALUES (%s, %s, NOW())
"""

SELECT_ALL_QUERY = "SELECT * FROM sensor_data"

SELECT_THRESHOLD_QUERY = """
SELECT * FROM sensor_data
WHERE moisture_level < %s
"""

UPDATE_QUERY = """
UPDATE sensor_data
SET moisture_level = %s
WHERE sensor_id = %s
"""

DELETE_QUERY = """
DELETE FROM sensor_data
WHERE sensor_id = %s
"""
