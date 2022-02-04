import pandas as pd
import plotly.express as px

df = pd.read_csv('covid.csv')

fig = px.scatter(df , 'date' , 'cases' , size = 'cases' , color = 'cases')

fig.show()