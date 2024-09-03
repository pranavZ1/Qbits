import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")
remainingDf = df.loc[df['status'] == 0]
doneDf = df.loc[df['status'] == 1]

print("===================================")
print("||   Welcome to the CRM Panel    ||")
print("===================================")

while True:
    df = pd.read_csv("data.csv")
    remainingDf = df.loc[df['status'] == 0]
    doneDf = df.loc[df['status'] == 1]
    print("Remaining leads: {}".format(remainingDf.shape[0]))
    print("Handled leads: {}".format(len(doneDf)))
    print("**************************")
    print("1. Handle next lead")
    print("2. Show remaining leads")
    print("3. Show handled leads")
    print("4. Exit")
    
    ch = int(input("Enter your choice"))

    if ch == 1:
        if len(remainingDf) == 0:
            print("No more leads to handle")
            break
        currentLead = remainingDf.iloc[0]
        print("Name: {} | Phone Number: {}".format(currentLead["Names"], currentLead["phoneNumbers"]))
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
                answer = "N/A"            
        df.loc[df['phoneNumbers'] == currentLead["phoneNumbers"],'result'] = str(answer)      
        df.loc[df['phoneNumbers'] == currentLead['phoneNumbers'],'status'] = 1
        df.to_csv("data.csv",index=False)
        print("Lead updated")
    elif ch == 2:
        for i in range(len(remainingDf)):
            print(" {} | {} ".format(remainingDf.iloc[i]['Names'], remainingDf.iloc[i]['phoneNumbers']))
    elif ch == 3:
        for i in range(len(doneDf)):
            print(" {} | {} | {} ".format(doneDf.iloc[i]['Names'], doneDf.iloc[i]['phoneNumbers'], doneDf.iloc[i]['result']))
    elif ch == 4:
        df.to_csv("data.csv",index=False)
        print("Data saved sucessfully!!!")
        break     
    else:
        print("Pls choose from the menu :(")

