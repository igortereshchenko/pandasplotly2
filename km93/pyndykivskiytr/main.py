
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot
#bq_assistant = BigQueryHelper('bigquery-public-data','epa_historical_air_quality')
bq_assistant = BigQueryHelper('bigquery-public-data','epa_historical_air_quality')

QUERY = """
		SELECT `state_name`, `date_local`, `arithmetic_mean`, `observation_count`
        FROM `bigquery-public-data.epa_historical_air_quality.co_daily_summary`
        LIMIT 1000
        """


df = bq_assistant.query_to_pandas(QUERY)

arithmetic_mean_count=df.groupby(['observation_count'])['arithmetic_mean'].count()

trace1 = go.Scatter(
	x=arithmetic_mean_count.index,
	y=arithmetic_mean_count.values
                    )
layout1= go.Layout(
	xaxis=dict(title="observation_count"),
	yaxis=dict(title='arithmetic_mean')
	)

figure1 = go.Figure(data=[trace1], layout=layout1)

trace2 = go.Pie(
	labels=arithmetic_mean_count.index,
    values=arithmetic_mean_count.values
                    )

layout2=go.Layout(
	title='data',
    xaxis=dict(title=''),
    yaxis=dict(title='')
	)

figure2 = go.Figure(data=[trace2], layout=layout2)

trace3 = go.Bar(

)

#data = [trace1]

layout = dict(
              title = '',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace2], layout = layout2)
plot(fig)

