import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquerry-public-data','pm10_daily_summary')


QUERY = """
        SELECT county_code, sample_duration, date_local, observation_count  FROM `bigquerry-public-data._pm10_daily_summary`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)


local_count_1 = df.grouphy(['county_code'])['observation_count'].count()
local_count_2 = df.grouphy(['county_code'])['observation_count'].count()
local_count_3 = df.grouphy(['county_code'])['observation_count'].count()

trace3  = go.Scatter(
    x = local_count_3.index,
    y = local_count_3.value,
    marker=dict(color='rgba(225, 174, 255, 0.5)')
)
trace2 = go.Scatter(
    x = local_count_2.index,
    y = local_count_2.value,
    marker=dict(color='rgba(225, 174, 255, 0.5)')

)

trace1 = go.Bar(
    x = local_count_1.index,
    y = local_count_1.value,
    marker = dict(color = 'rgba(225, 174, 255, 0.5)')
)

layout3 = go.Layout(
              title = 'Observation_count relatively county_code',
              xaxis = dict(title = 'county_code'),
              yaxis = dict(title = 'observation_count')
)

layout2 = go.Layout(
              title = 'Observation_count relatively county_code',
              xaxis = dict(title= 'county_code'),
              yaxis = dict(title='observation_count')
)



figure1 = go.Figure(data = [trace1], layout = layout1)
figure2 = go.Figure(data = [trace2], layout = layout2)
figure3 = go.Figure(data = [trace3])
