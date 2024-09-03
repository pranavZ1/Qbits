import numpy as np
import pandas as pd
import sqlite3
from nanoid import generate
import plotly.express as px


conn = sqlite3.connect('test.db')
cursor = conn.cursor()

def login():
    while True:
        print("Enter your name:")
        name = input()
        res = cursor.execute("SELECT * FROM user WHERE name = '{}'".format(name)).fetchall()
        if len(res) == 0:
            print("Wrong name")
        else:
            print("Welcome {}".format(name))
            break
    return res[0][0]

def getData(bda_id):
    return cursor.execute("SELECT * FROM sales WHERE bda_id = '{}'".format(bda_id)) .fetchall()

def splitData(data):
    handled_data = []
    unhandled_data = []
    for i in data:
        if i[4] == 1:
            handled_data.append(i)
        else:
            unhandled_data.append(i)
    return handled_data,unhandled_data


print("===================================")
print("||   Welcome to the CRM Panel    ||")
print("===================================")
bda_id = login()
print("===================================")

while True:
    print("===============Main Menu=============")
    data = getData(bda_id)
    handled_data,unhandled_data = splitData(data)
    print("Handled data: ",len(handled_data))
    print("Unhandled data: ",len(unhandled_data))
    print()
    print("1. Handled Next lead")
    print("2. View handled data")
    print("3. View unhandled lead")
    print("4. Analyze")
    print("5. Exit")
    print("===================================")
    print("Enter your choice:")
    choice = int(input())
    print()
    if choice == 4:
        print("Thank You")
    elif choice == 1:
        if len(unhandled_data) == 0:
            print("No Unhandled data")
            continue
        print("Next lead:")
        current_lead = cursor.execute("SELECT * FROM sales WHERE bda_id = '{}' AND lead_status = 0".format(bda_id)).fetchone()  
        if current_lead == None:
            print("No Unhandled data")
            continue
        print("Name: ",current_lead[2])
        print("Phone Number: ",current_lead[3])
        print("Make the call and enter the result from the options")
        print("1. Intrested")
        print("2. Not Interested")
        print("3. Call Back Later")
        print("4. DNP (Did Not Pick)")
        print("5. Junk Lead/Wrong Number")
        res = int(input("Enter the result:"))
        match(res):
            case 1:
                print("Lead is intersted")
                answer = "Interested"
            case 2:
                print("Lead is not interested")
                answer = "Not Interested"    
            case 3:
                print("Lead asked to call back later")
                answer = "Call Back Later"   
            case 4:
                print("Lead Did Not pick the call")
                answer = "DNP (Did Not Pick)"
            case 5:
                print("Lead is junk/wrong number")
                answer = "Junk Lead/Wrong Number" 
            case _:
                print("Invalid Option")
        cursor.execute("UPDATE sales SET lead_status = 1,lead_result ='{}' WHERE id = '{}'"
                       .format(answer,current_lead[0]))
        conn.commit()
        print("Lead Updated")
    elif choice == 2:
        print("Handled data: ")
        print(" Names || phone numbers || results")
        for i in handled_data:
            print(i[2],i[3],i[5])
    elif choice == 3:
        print("Unhandled Data")
        print(" Names || phone numbers || results")
        for i in unhandled_data:
            print(i[2],i[3],i[5])
    elif choice == 4:
        df = pd.DataFrame([i[5] for i in data],columns=["Result"])
        values = df["Result"].value_counts.to_list()
        names = df["Result"].value_counts.index.to_list()
        colors = ['gold','mediumtorquoise','darkorange','lightgreen','red']
        fig = px.pie(df,values=values,names=names,title='Lead Results')
        fig.update_traces(
            textposition = 'inside',
            textinfo = 'percent+label',
            marker = dict(colors = colors,line = dict(color = '#000000',width = 2))
        )
        fig.write_html('lead_results1.html',auto_open=True)

