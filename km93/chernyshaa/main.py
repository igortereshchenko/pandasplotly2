import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquerry-public-data','pm10_daily_summary')


QUERY = """
        SELECT county_code, sample_duration, date_local, observation_count  FROM 'bigquerry-public-data._pm10_daily_summary'
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)


local_count = df.grouphy(['county_code'])['observation_count'].count()

trace3 = go.Bar(
    x = local_count.index,
    y = local_count.value,
    marker = dict(color = 'rgba(225, 174, 255, 0.5)'
)

layout = go.Layout(
              title = 'Observation_count relatively county_code',
              xaxis = dict(title= 'county_code'),
              yaxis = dict(title='observation_count')
)


figure1 = go.Figure(data = [trace3], layout = layout)
