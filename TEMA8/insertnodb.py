import sqlite3
import psutil


conn = sqlite3.connect("sensors.db")
cursor = conn.cursor()

# Na variável 'conn' colocamos a conexão com o BD
# A variável 'cursor' é criada, do tipo "cursor"

# Prepare the sql statement for the new location
sql = """
    INSERT INTO location (name, description) 
    VALUES (?, ?)
"""

data = ("Prometheus Server", "Prometheus Server @ lab. 163 / ISE /UAlg")

# Execute the sql statement and get the new location id
cursor.execute(sql, data)

location_id = cursor.lastrowid
location_id # Salva o id do último dado upado, para não haver sobrescrita  
conn.commit()

sql = """
    INSERT INTO Unit (unit, description) 
    VALUES (?, ?)
"""

data = ("percent", "percentage of usage")

cursor.execute(sql, data)  # statement + tupla com os dados
conn.commit()


sql = """
    INSERT INTO Sensor (idLocation, name, unit)
    VALUES (:idLocation, :name, :unit)
"""

data = {
    "idLocation": location_id,
    "name": "cpu_sensor_01",
    "unit": "percent",
}

cursor.execute(sql, data)
sensor_id = cursor.lastrowid
conn.commit()
sensor_id

sql = """
    INSERT INTO Reading (idSensor, value)     
    VALUES (:idSensor, :value)
"""

for _ in range(20):
    data = {
        "idSensor": sensor_id, # Id da cell de dados (neste caso, uso de CPU)
        "value": psutil.cpu_percent(interval=1), # Retorna o uso médio de CPU no último segundo
    }
    cursor.execute(sql, data)
    conn.commit()
    print(".", end="") # No fim de cada execução terá um '.'

cursor.close()
conn.close()