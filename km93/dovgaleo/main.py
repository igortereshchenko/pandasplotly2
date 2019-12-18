import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('epa_historical_air_quality', 'co_hourly_summary')

QUERY = """
        SELECT `state_code`, `date_local`, `sample_measurement`, `units_of_measure` 
        FROM `bigquery-public-data.epa_historical_air_quality.co_hourly_summary`
        LIMIT 1000
        """

df = bq_assistant.query_to_pandas(QUERY)

trace1 = go.Scatter(
    x=df['date_local'],
    y=df['sample_measurement']
)
trace2 = go.Bar(
    x=df['date_local'],
    y=df['sample_measurement']
)
trace3 = go.Pie(
)

data = [trace2]

layout = dict(
    title='Measurement per day in millions',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Measurement per million')
)

fig = dict(data=[trace2], layout=layout)
plot(fig)