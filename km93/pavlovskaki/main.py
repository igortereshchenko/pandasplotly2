import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

bq_assistant = BigQueryHelper('bigquery-public-data','epa_historical_air_quality')


QUERY = """
        SELECT `state_code`,`time_local`,`sample_measurement`,`units_of_measure` FROM`bigquery-public-data.epa_historical_air_quality.hap_hourly_summary`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)

_sample_measurement_count = df.groupby(['time_local'])['sample_measurement'].count()

trace1 = go.Bar(
    x=_sample_measurement_count.index,
    y=_sample_measurement_count.values
)
layout1 = go.Layout(
    title='Код Fibs відносно виміряних значень',
    xaxis=dict(title='Виміряні значення'),
    yaxis=dict(title='Код Fibs')
)
figure1 = go.Figure(data=[trace1], layout=layout1)