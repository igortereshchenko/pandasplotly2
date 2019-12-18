import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','epa_historical_air_quality')

QUERY = """
		SELECT `state_code`, `date_local`, `mdl`, `parameter_name`
        FROM `bigquery-public-data.epa_historical_air_quality.co_hourly_summary`
        LIMIT 1000
        """


df = bq_assistant.query_to_pandas(QUERY)

state_code_count=df.groupby(['state_code'])['parameter_name'].count()
date_local_count=df.groupby(['date_local'])['parameter_name'].count()
mdl_count=df.groupby(['mdl'])['parameter_name'].count()
trace1 = go.Scatter(
	x=state_code_count.index,
	y=state_code_count.values
                    )
trace2 = go.Pie(
	labels=date_local_count.index,
    values=date_local_count.values
                    )

trace3 = go.Bar(
	x=mdl_count.index,
	y=mdl_count.values
)

layout1= go.Layout(
	xaxis=dict(title='state_code'),
	yaxis=dict(title='parmater_name')
	)
layout2=go.Layout(
	title='data',
    xaxis=dict(title=''),
    yaxis=dict(title='')
	)

figure1 = go.Figure(data=[trace1], layout=layout1)
figure2 = go.Figure(data=[trace2], layout=layout2)
fig = dict(data = [trace3])