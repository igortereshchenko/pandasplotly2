import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"


import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper("bigquery-public-data", "epa_historical_air_quality")


QUERY = """
        SELECT state_code, sample_duration, date_local, observation_count
        FROM `bigquery-public-data.epa_historical_air_quality.lead_daily_summary`
        LIMIT 10
        """


df = bq_assistant.query_to_pandas(QUERY)
print(df)




trace1 = go.Scatter(
                        x=df["sample_duration"].index,
                        y=df["date_local"],
                        mode="lines"

                    )

trace2 = go.Pie(

                        labels=df["date_local"],
                        values=df["date_local"].index,

                    )




data = [trace1, trace2]

layout = dict(
              title = '',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace1, trace2], layout = layout)
plot(fig)
