import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

bq_assistant = BigQueryHelper('bigquery-public-data','epa_historical_air_quality')


QUERY = """
        SELECT `state_code`,`parameter_name`,`observation_count`,`arithmetic_mean` FROM`bigquery-public-data.epa_historical_air_quality.nonoxnoy_daily_summary`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)

_param_name_count = df.groupby(['parameter_name'])['state_code'].count()
__observation_count = df.groupby(['parameter_name'])['observation_count'].count()
arithmetic_mean_count=df.groupby(['arithmetic_mean'])['parameter_name'].count()
trace1 = go.Bar(
    x=_param_name_count.index,
    y=_param_name_count.values
)

trace2 = go.Scatter(
    x=__observation_count.index,
    y=__observation_count.values,
    mode='lines'
                    )
trace3 = go.Bar(
	x=arithmetic_mean_count.index,
	y=arithmetic_mean_count.values
)
layout1 = go.Layout(
    title='Код Fibs відносно назв параметрів',
    xaxis=dict(title='вид газу'),
    yaxis=dict(title='ккість тонн')
)
layout2 = go.Layout(
    title='вид газу відносно ваги',
    xaxis=dict(title='вид газу'),
    yaxis=dict(title='ккість тонн'),
)

figure1 = go.Figure(data=[trace1], layout=layout1)
figure2 = go.Figure(data=[trace2], layout=layout2)
plot(figure1)
plot(figure2)
fig = dict(data = [trace3])
plot(fig)