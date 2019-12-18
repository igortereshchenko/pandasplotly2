import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'epa')


QUERY = """
        SELECT state_name, year, observation_percent, sample_duration
        FROM `bigquery-public-data.epa.epa-historical-air-quality`
        LIMIT 10
        """


df = bq_assistant.query_to_pandas(QUERY)


print(df.head(3))

df_observation_state = df.groupby(['state_name'])['observation_percent'].average()

trace1 = go.Scatter(

)



trace2 = go.Pie(

                    )

trace3 = go.Bar(
x = df_observation_state.index,
    y = df_observation_state.values,
    name = 'Observation percent depending on state'
)

data = [trace3]

layout = dict(
              title = 'Observations',
              xaxis= dict(title= 'state'),
              yaxis=dict(title='average observation percent'),
             )
fig = dict(data = [trace3], layout = layout)
plot(fig)
