import sqlite3
import pandas as pd
from datetime import datetime as d
from nanoid import generate

conn = sqlite3.connect('test.db')
print("Opened database sucessfully")

df = pd.read_csv('support_leads.csv')
print("Data loaded sucessfully")
print("Shape of the data: ",df.shape)

cursor =conn.cursor()
print("Enter your name:")
name = input()
res = cursor.execute("SELECT * FROM user WHERE name = '{}'".format(name)).fetchall()
if len(res) == 0:
    print("Wrong name")
else:
    print("Welcome {}".format(name))
bda_id = res[0][0]
print(bda_id)


names = df['Names']
mobiles = df['phoneNumbers']
ids = [generate() for _ in range(len(names))]
bda_ids = [bda_id for _ in range(len(names))]
lead_status = [0 for _ in range(len(names))]
lead_result = ["Unhandled" for _ in range(len(names))]

data = []
for i in range(len(names)):
    t = tuple([ids[i],bda_ids[i],names[i],mobiles[i],lead_status[i],lead_result[i]])
    data.append(t)

print("Data Prepared")

cursor.executemany("INSERT INTO sales(id,bda_id,lead_name,lead_number,lead_status,lead_result) VALUES (?,?,?,?,?,?)",data)
conn.commit()
print("Data inserted successfully")
conn.close()