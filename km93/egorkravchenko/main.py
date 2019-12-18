import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

bq_assistant = BigQueryHelper("bigquery-public-data", "epa_historical_air_quality")


QUERY = """
        SELECT `county_code`, `site_num`, `observation_count`, `observation_percent` FROM 
        `bigquery-public-data.epa_historical_air_quality.o3_daily_summary`
        LIMIT 100
        """

df = bq_assistant.query_to_pandas(QUERY)

_observation_percent_count = df.groupby('site_num')["observation_percent"].count()
_observation_count_count = df.groupby('country_code')["observation_count"].count()
trace1 = go.Bar(
    x=_observation_percent_count.index,
    y=_observation_percent_count.values
)
trace2 = go.Scatter(
    x=_observation_count_count.index,
    y=_observation_count_count.values,
    mode='lines'
)

layout1 = go.Layout(
    title='bar',
    xaxis=dict(title='site_num'),
    yaxis=dict(title='observation_percent'),
)

layout2 = go.Layout(
    title='scatter',
    xaxis=dict(title='country_code'),
    yaxis=dict(title='observation_count'),
)
fig1 = go.Figure(data=[trace1], layout=layout1)
fig2 = go.Figure(data=[trace2], layout=layout2)

plot(fig1)
plot(fig2)