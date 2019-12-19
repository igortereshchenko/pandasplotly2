import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'epa_historical_air_quality')

QUERY = """
        SELECT state_name, year, observation_percent, sample_duration
        FROM `bigquery-public-data.epa_historical_air_quality.air_quality_annual_summary`
        LIMIT 100
        """

df = bq_assistant.query_to_pandas(QUERY)

print(df.head(3))

df_observation_year = df.groupby(['year'])['observation_percent'].mean()
df_observation_sample_duration = df.groupby(['sample_duration'])['observation_percent'].mean()

trace1 = go.Scatter(

    x = df_observation_year.index,
    y = df_observation_year.values,
    name = 'Observation percent depending on year',
    mode = 'lines+markers'
)

trace2 = go.Pie(
    labels = df_observation_year.index,
    values = df_observation_year.values,
    name = 'Observation percent depending on year'

)

trace3 = go.Bar(
    x=df_observation_sample_duration.index,
    y=df_observation_sample_duration.values,
    name='Observation percent depending on sample duration'
)

data1 = [trace1]
data2 = [trace2]
data3 = [trace3]

layout1 = dict(title = 'Observations percent',xaxis= dict(title= 'year'),
               yaxis=dict(title='average observation percent'))
layout2 = dict(title = 'Observations percent',xaxis= dict(title= 'year'),
               yaxis=dict(title='average observation percent'))
layout3 = dict(title='Observations percent', xaxis=dict(title='sample duration'),
               yaxis=dict(title='average observation percent'))

fig = dict(data=data2, layout=layout2)
plot(fig)
