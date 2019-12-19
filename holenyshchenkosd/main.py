import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper(,)
client = bigquery.client()

QUERY = '''SELECT state_code, observation_count, observation_percent, arithmetic_mean 
           FROM `bigquery_public_data.epa_historical_air_quality.co_daily_summary`
        LIMIT 10000'''


df = bq_assistant.query_to_pandas(QUERY)





trace1 = go.Scatter(df,
  x='observation_count', 
  y='observation_percent'
                    )



trace2 = go.Pie(df, 
  x='observation_percent'
                    )

trace3 = go.Bar(df,
  y='arithmetic_mean'
)

data = [trace1]
 
 layout = dict(
              title = '',
              xaxis= dict(title= 'observation_count'),
              yaxis=dict(title='observation_percent'),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)
