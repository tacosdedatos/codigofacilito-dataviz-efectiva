import streamlit as st
import altair as alt 
from vega_datasets import data as vega_data
import pandas as pd

import datetime 

import altair as alt
from vega_datasets import data

source = data.seattle_weather()

scale = alt.Scale(domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
                  range=['#e7ba52', '#a7a7a7', '#aec7e8', '#1f77b4', '#9467bd'])
color = alt.Color('weather:N', scale=scale)


st.markdown("# Grafico de Seattle")

# dropdown de valores de años
columna_1, columna_2 = st.columns(2)

with columna_1:
    fecha_comienzo = st.date_input(label = 'Escoge la fecha comienzo', value = datetime.datetime(2012,1,1), min_value =datetime.datetime(2012,1,1), max_value=datetime.datetime(2015,12,31))
    fecha_comienzo = pd.to_datetime(fecha_comienzo)
with columna_2:
    fecha_final = st.date_input(label = 'Escoge la fecha final', value = datetime.datetime(2015,12,31), min_value =datetime.datetime(2012,1,1), max_value=datetime.datetime(2015,12,31))
    fecha_final = pd.to_datetime(fecha_final)

subset = source[(source['date'] >= fecha_comienzo) & (source['date'] <= fecha_final)]


# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=['x'])
click = alt.selection_point(encodings=['color'])

# Top panel is scatter plot of temperature vs time
points = alt.Chart().mark_point().encode(
    alt.X('monthdate(date):T', title='Date'),
    alt.Y('temp_max:Q',
        title='Maximum Daily Temperature (C)',
        scale=alt.Scale(domain=[-5, 40])
    ),
    color=alt.condition(brush, color, alt.value('lightgray')),
    size=alt.Size('precipitation:Q', scale=alt.Scale(range=[5, 200]))
).properties(
    width=550,
    height=300
).add_params(
    brush
).transform_filter(
    click
)

# Bottom panel is a bar chart of weather type
bars = alt.Chart().mark_bar().encode(
    x='count()',
    y='weather:N',
    color=alt.condition(click, color, alt.value('lightgray')),
).transform_filter(
    brush
).properties(
    width=550,
).add_params(
    click
)

final = alt.vconcat(
    points,
    bars,
    data=subset,
    title="Seattle Weather: 2012-2015"
)


st.altair_chart(final)