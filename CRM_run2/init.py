import numpy as np
import pandas as pd

df = pd.read_csv('support_leads.csv')
print("Data loaded Sucesssully!!!")
print("Shape:",df.shape)
df['status'] = 0
df['result'] = 'Unhandled'
df.to_csv('data.csv',index=False)
print("Data.csv created sucessfully!!")