import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('epa_historical_air_quality' ,'bigquery-public-data')


QUERY = """
        SELECT state_code, sample_duration, date_local,  units_of_measure  FROM bigquery-public-data.epa_historical_air_quality.lead_daily_summary
        LIMIT 100
        """

_sample_duration_count = df.groupby(['date_local'])['sample_duration'].count()
_units_of_measure_count = df.groupby(['date_local'])['units_of_measure'].count()
_code_count = df.groupby(['date_local'])['code_count'].count()
trace1 = go.Bar(
    x=_sample_duration_count.index,
    y=_sample_duration_count.values
)
trace2 = go.Pie(
    x=_units_of_measure_count.index,
    y=_units_of_measure_count.values
)
trace3 = go.Scatter(
    x=_code_count.index,
    y=_code_count.values,
    mode='lines'
)
layout1 = go.Layout(
    title='Дата відносно часу',
    xaxis=dict(title='Тривалість часу'),
    yaxis=dict(title='Дата')
)
layout3 = go.Layout(
    title='Стан  відносно дати',
    xaxis=dict(title='дата'),
    yaxis=dict(title='Стан')
)

figure1 = go.Figure(data=[trace1], layout=layout1)
plot(figure1)
figure2 = go.Figure(data=[trace2], layout=layout2)
plot(figure2)
figure3 = go.Figure(data=[trace2], layout=layout2)
plot(figure3)