import pandas as pd
import plotly.express as px

df = pd.read_csv('covid.csv')

fig = px.scatter(df , 'date' , 'cases' , size = 'country' , color = 'country')

fig.show()
