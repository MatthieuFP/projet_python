from src.projet_python import CsvDataframe
from src.support.constants import *
from src.support.my_logger import logger

import plotly.graph_objs as go
import plotly.offline as offline

#Vérification avec un graphe de la distance par rapport au prix

Data = CsvDataframe(nrows=100000)
df = Data.df

trace0 = go.Scatter(
    x=df[Distance],
    y=df[Fare_amount],
    mode='markers')

layout = go.Layout(
    xaxis=dict(
        title='Distance (km)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Prix (USD)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

data = [trace0]
fig = go.Figure(data=data, layout=layout)

offline.plot(fig, image='png', filename=Root_graphs + r"\distance_prix.html")

logger.info("graph ploted")
