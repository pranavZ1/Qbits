import pandas as pd
import plotly.express as px
df = pd.read_csv('data.csv')
values = df['result'].value_counts().to_list()
names = df['result'].value_counts().index
colors = ['gold','mediumtorquoise','darkorange','lightgreen','red']
fig = px.pie(df,values=values,names=names,title='Lead Results')
fig.update_traces(
    textposition = 'inside',
    textinfo = 'percent+label',
    marker = dict(colors = colors,line = dict(color = '#000000',width = 2))
)
fig.write_html('lead_results.html',auto_open=True)