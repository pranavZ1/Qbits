import sqlite3
from datetime import datetime as d
from nanoid import generate


conn = sqlite3.connect('test.db')
print("Connection established")

conn.execute('''CREATE TABLE IF NOT EXISTS user
             (id TEXT PRIMARY KEY NOT NULL,
             name TEXT NOT NULL,
             mobileNumber TEXT NOT NULL,
             role TEXT NOT NULL,
             address TEXT)''')


conn.execute('''CREATE TABLE IF NOT EXISTS sales
             (id TEXT PRIMARY KEY NOT NULL,
             bda_id TEXT NOT NULL,
             lead_name TEXT NOT NULL,
             lead_number TEXT NOT NULL,
             lead_status INTEGER NOT NULL,
             lead_result TEXT NOT NULL,
             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
             FOREIGN KEY (bda_id) REFERENCES user(id)
             )''')

conn.execute("INSERT INTO user (id, name, mobileNumber, role, address) VALUES ('{}', 'TL ONE', 11111111, 'TL', 'Bangalore');".format(generate()))


conn.commit()

conn.close()