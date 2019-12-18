
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper("bigquery-public-data", "epa_historical_air_quality")

QUERY = """
	SELECT state_name, sample_measurement, date_local, mdl
	FROM `bigquery-public-data.epa_historical_air_quality.co_hourly_summary`
	LIMIT 10
	"""

df = bq_assistant.query_to_pandas(QUERY)
print(df)

trace1 = go.Scatter(
	x=df["sample_measurement"].index,
	y=df["mdl"],
	mode="lines"
		)
trace2 = go.Pie()
trace3 = go.Bar(
			x=df["sample_measurement"].index,
			y=df["mdl"]
)

data = [trace1,trace2,trace3]

layout = dict(
	title='',
	xaxis=dict(title='day'),
	yaxis=dict(title='sample measurement')
)
fig = dict(data=[trace1,trace2, trace3], layout=layout)
plot(fig)