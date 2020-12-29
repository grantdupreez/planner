import streamlit as st
import pandas as pd
import plotly.figure_factory as ff

uploaded_file = st.sidebar.file_uploader("Choose a file",type=['CSV'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, header=[0], parse_dates=[1])
    st.write(df)
    
    fig = ff.create_gantt(df, index_col='Status', show_colorbar=True,
                         group_tasks=True, showgrid_x=True, showgrid_y=True)
 
    fig
    
