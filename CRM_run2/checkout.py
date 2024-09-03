import pandas as pd
df = pd.read_csv('data.csv')
data = df['result'].value_counts()
rate = 2100
print("Total leads = ",len(df))
print("Handled leads = ",len(df[df['status'] == 1]))
print("Remaining leads = ",len(df[df['status'] == 0]))
print("Total conversions = ",data['Interested'])
print("Total Rejections = ",data['Not Interested'] + data['Junk Lead/Wrong Number'])
print("Recycled Leads = ",data['DNP (Did Not Pick)'] + data['Call Back Later'])
print("Payment = {} * {} = {} Rs ".format(data['Interested'],rate,data['Interested']*rate))