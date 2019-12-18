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

df_observation_sample_duration = df.groupby(['sample_duration'])['observation_percent'].mean()

trace1 = go.Scatter(

)

trace2 = go.Pie(

)

trace3 = go.Bar(
    x=df_observation_sample_duration.index,
    y=df_observation_sample_duration.values,
    name='Observation percent depending on sample duration'
)

data3 = [trace3]

layout3 = dict(title='Observations', xaxis=dict(title='sample duration'),
               yaxis=dict(title='average observation percent'))

fig = dict(data=data3, layout=layout3)
plot(fig)
