import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

bq_assistant = BigQueryHelper('bigquery-public-data','epa_historical_air_quality')


QUERY = """
        SELECT `county_code`,`observation_count`,`observation_percent`,`valid_day_count` FROM`bigquery-public-data.epa_historical_air_quality.hap_hourly_summary`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)

_sample_measurement_count = df.groupby(['county_code'])['observation_count'].count()
__local_count = df.groupby(['county_code'])['observation_percent'].count()
__units_of_measure__count = df.groupby(['county_code'])['valid_day_count'].count()

trace1 = go.Bar(
    x=_sample_measurement_count.index,
    y=_sample_measurement_count.values
)

trace2 = go.Scatter(
    x=__local_count.index,
    y=__local_count.values,
    mode='lines'
                    )
trace3 = go.Pie(
    labels=__units_of_measure__count.index,
    values=__units_of_measure__count.values,
)
layout1 = go.Layout(
    title='Код Fibs відносно виміряних значень',
    xaxis=dict(title='Виміряні значення'),
    yaxis=dict(title='Код Fibs')
)
layout2 = go.Layout(
    title='he number of days during the year where the daily monitoring criteria were met',
    xaxis=dict(title='The percent representing the number of observations taken with respect to the number scheduled to be taken'),
    yaxis=dict(title='he number of observations (samples) taken during the year.'),
)

figure1 = go.Figure(data=[trace1], layout=layout1)
figure2 = go.Figure(data=[trace2], layout=layout2)
figure3 = go.Figure(data=[trace3])
plot.figure1