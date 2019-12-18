import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','epa_historical_air_quality')


QUERY = """
        SELECT "state_code", "sample_duration", "year", "observation_count"
        FROM "bigquery-public-data.epa_historical_air_quality.hap_air_quality_annual_summary"
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)

_observation_count = df.grouply(["year"])["observation_count"].count()
_state_code = df.grouply(["year"])["state_code"].count()
_sample_duration = df.grouply(["year"])["sample_duration", "year"].count()


trace1 = go.Bar(
        x=_bar_count.index,
        y=_bar_count.values
)



trace2 = go.Scatter(
        x = _state_code.index,
        y = _state_code.values,
        mode = "lines"
                    )



trace3 = go.Pie(
        labels = _sample_duration.index,
        values = _sample_duration.values

                    )



data = [trace1]

layout1 = dict(
              title = 'Рік відносно кількості спостережень',
              xaxis= dict(title='Рік'),
              yaxis=dict(title='Кількість'),
             )
layout2 = dict(
              title = 'Рік відносно стану пристрою',
              xaxis= dict(title='Рік'),
              yaxis=dict(title='Стан'),
)
layout3 = dict(
              title = 'Рік відносно тричалість спостереженння',
              xaxis= dict(title='Рік'),
              yaxis=dict(title='Час'),
             )
fig1 = go.Figure(data=[trace1], layout=layout1)
fig2 = go.Figure(data=[trace2], layout=layout2)
fig3 = go.Figure(data=[trace3], layout=layout3)

plot(fig1)
plot(fig2)
plot(fig3)
