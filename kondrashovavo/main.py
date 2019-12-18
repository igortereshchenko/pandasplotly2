import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','hap_hourly_summary')


QUERY = """
        SELECT 'country-name','date-local','sample-measurement', 'method-code'
        FROM  'bigquery-public-data.epa_historical_air_quality.epa_hap_hourly_summary'
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)






trace1 = go.Scatter(
    x = df_observation_.date_local,
    y = df_observation_state.sample_measurement,
    mode = 'lines+markers',
    name = 'Observation percent depending on state'

                    )



trace2 = go.Pie(
    labeles = _country_name_count.index
    values =  _country_name_count.values
                    )

trace3 = go.Bar(
    x = _sample_measurement_count.index,
    y = __sample_measurement_count.values

)

data = [trace1]

layout = dict(
              title = 'data',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)

