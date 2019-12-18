import os
import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

bq_assistant = BigQueryHelper("bigquery-public-data",'epa_historical_air_quality')


QUERY = """
        SELECT time_local, sample_measurement, units_of_measure, state_name 
        FROM `bigquery-public-data.epa_historical_air_quality.pm25_frm_hourly_summary`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)

_1 = df.groupby(['time_local'])['sample_measurement'].count()
_3= df.groupby(['time_local'])['state_name'].count()
_2= df.groupby(['sample_measurement'])['state_name'].count()
trace1 = go.Bar(
    x=_1.index,
    y=_1.values
)
trace2 = go.Scatter(
    x=_2.index,
    y=_2.values,
    mode='lines'
)
trace3= go.Pie(
        labels = _3.index,
        values= _3.values,)

layout1 = go.Layout(
    title='Заміри відносно часу',
    xaxis=dict(title='Час'),
    yaxis=dict(title='Заміри')
)

layout2 = go.Layout(
    title='Заміри відносно штату',
    xaxis=dict(title='Заміри'),
    yaxis=dict(title='Штат'),
)

figure1 = go.Figure(data=[trace1], layout=layout1)

figure2 = go.Figure(data=[trace2], layout=layout2)

figure3 = go.Figure(data=[trace3])
