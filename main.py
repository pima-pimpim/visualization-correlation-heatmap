import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Modgut Database")

region = pd.read_csv('region_personal.csv')

st.image("Criteria.png")

option = st.selectbox(
    'Please select a criteria',
    ('gender', 'age_group', 'bmi_group', 'region'))

st.write('You criteria:', option)

#show_btn = st.button("Display!")
#if show_btn:
for i in ('gender', 'age_group', 'bmi_group', 'region'):
    if i in option:
        # Create distplot with custom bin_size
        fig = px.pie(region[option].value_counts(), values=region[option].value_counts().values, names=region[option].value_counts().index)
        fig.update_traces(hoverinfo='label+value', textinfo='label+value+percent')

        # Plot!
        st.plotly_chart(fig)

st.markdown("Last updated: Nov 19, 2024.")