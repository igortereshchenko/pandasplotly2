import os
import pandas as pd
import pandas.core.frame
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

bq_assistant = BigQueryHelper('bigquery-public-data', 'epa_historical_air_quality.no2_daily_summary')


QUERY = """
        SELECT sample_duration, date_local, units_of_measure, county_name
        FROM bigquery-public-data.epa_historical_air_quality.no2_daily_summary
        LIMIT 100
        """


df: pandas.core.frame.DataFrame = bq_assistant.query_to_pandas(QUERY)

df_group_by_county_name = df.groupby(['county_name'])
df.num_of_samples = df_group_by_county_name["sample_duration"].count()

trace1 = go.Scatter(
    x = df.num_of_samples.index,
    y = df.num_of_samples.values,
    mode = "lines+markers",
    name = "num of samples"
)



trace2 = go.Pie(

                    )

trace3 = go.Bar(
    x=df.num_of_samples.index,
    y=df.num_of_samples.values
)

data = [trace1]

layout = dict(
              title='',
              xaxis=dict(title=''),
              yaxis=dict(title=''),
             )
fig = dict(data=[trace1], layout=layout)
plot(fig)
fig_bar = go.Figure(data=[trace3], layout=layout)
plot(fig_bar)