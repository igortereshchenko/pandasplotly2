import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquerry-public-data','epa_historical_air_quality')


QUERY = """
        SELECT `state_name`,`sample_measurement`,`date_gmt`,`parameter_name`
        FROM `bigquery-public-data.epa_historical_air_quality.nonoxnoy_hourly_summary`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)

_sample_measurement_count = df.groupby(["state_name"])["sample_measurement"].count()
_date_gmt_count = df.groupby(["state_name"])["date_gmt"].count()
_parameter_name_count = df.groupby(["state_name"])["parameter_name"].count()




trace1 = go.Scatter(x=_date_gmt_count.index,
                    y=_date_gmt_count.values,)




trace2 = go.Pie(
    labels=_parameter_name_count.index,
    values=_parameter_name_count.values)

trace3 = go.Bar(
    x =_sample_measurement_count.index,
    y =_sample_measurement_count.values)



layout1 = go.Layout(
              title = 'Date',
              xaxis= dict(title= 'Values'),
              yaxis=dict(title='Код Fibs'),
             )


layout2 = go.Layout(
              title = 'Date',
              xaxis= dict(title= 'Values'),
              yaxis=dict(title='Код Fibs'),
             )

layout3 = go.Layout(
              title = 'sample_measurement',
              xaxis= dict(title= 'Values'),
              yaxis=dict(title='Код Fibs'),
             )
figure1 = go.Figure(data = [trace1], layout = layout1)
figure2 = go.Figure(data = [trace2], layout = layout2)
figure3 = go.Figure(data = [trace3], layout = layout3)

plot(figure3)
plot(figure1)
plot(figure2)