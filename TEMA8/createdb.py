import sqlite3


sql = """
CREATE TABLE
    Location (
        idLocation INTEGER CONSTRAINT Location_pk PRIMARY key autoincrement,
        name TEXT NOT NULL,
        description text NOT NULL
    );

CREATE TABLE
    Unit (
        unit text CONSTRAINT Unit_pk PRIMARY key,
        description text NOT NULL
    );

CREATE TABLE
    Sensor (
        idSensor INTEGER CONSTRAINT Sensor_pk PRIMARY key autoincrement,
        idLocation INTEGER NOT NULL CONSTRAINT Sensor_Location_idLocation_fk REFERENCES Location ON UPDATE cascade ON DELETE cascade,
        name text NOT NULL,
        unit text NOT NULL CONSTRAINT Sensor_Unit_unit_fk REFERENCES Unit ON UPDATE cascade ON DELETE cascade
    );

CREATE TABLE
    Reading (
        idReading INTEGER CONSTRAINT Reading_pk PRIMARY key autoincrement,
        idSensor INTEGER CONSTRAINT Reading_Sensor_idSensor_fk REFERENCES Sensor ON UPDATE cascade ON DELETE cascade,
        TIMESTAMP datetime DEFAULT CURRENT_TIMESTAMP,
        VALUE REAL NOT NULL
    );

CREATE TABLE
    Alert (
        idAlert INTEGER CONSTRAINT Alert_pk PRIMARY key autoincrement,
        idSensor INTEGER CONSTRAINT Alert_Sensor_idSensor_fk REFERENCES Sensor ON UPDATE cascade ON DELETE cascade,
        description text NOT NULL,
        cleared INTEGER
    )
"""

with sqlite3.connect("sensors.db") as conn:
    cursor = conn.cursor()
    
    # executescript is a nonstandard convenience method for executing multiple SQL statements at once.
    cursor.executescript(sql)
    
    #cursor.close() # not needed, as it is closed automatically when the with block ends