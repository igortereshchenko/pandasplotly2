import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('epa_historical_air_quality' ,'bigquery-public-data')


QUERY = """
        SELECT state_code, sample_duration, date_local,  units_of_measure  FROM bigquery-public-data.epa_historical_air_quality.lead_daily_summary
        LIMIT 300
        """

_sample_duration_count = df.groupby(['date_local'])['sample_duration'].count()

trace1 = go.Bar(
    x=_sample_duration_count.index,
    y=_sample_duration_count.values
)
layout1 = go.Layout(
    title='Дата відносно часу ',
    xaxis=dict(title='Тривалість часу'),
    yaxis=dict(title=' Дата ')
)
figure1 = go.Figure(data=[trace1], layout=layout1)
plot(figure1)