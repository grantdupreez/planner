import streamlit as st
import pandas as pd
import plotly.figure_factory as ff

uploaded_file = st.sidebar.file_uploader("Choose a file",type=['CSV'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, header=[0], parse_dates=[1])
    st.write(df)
    
#    colors = {'Not Started': 'rgb(220, 0, 0)',
#          'Incomplete': (1, 0.9, 0.16),
#          'Complete': 'rgb(0, 255, 100)'}

#   fig = ff.create_gantt(df, colors=colors, index_col='Status', show_colorbar=True,
#                      group_tasks=True)

    fig = ff.create_gantt(df, index_col='Project_ID', show_colorbar=True,
                          showgrid_x=True, showgrid_y=True)
 
    fig
    
    
    
#df = [dict(Task="Job-1", Start='2017-01-01', Finish='2017-02-02', Resource='Complete'),
#      dict(Task="Job-1", Start='2017-02-15', Finish='2017-03-15', Resource='Incomplete'),
#      dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Not Started'),
#      dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Complete'),
#      dict(Task="Job-3", Start='2017-03-10', Finish='2017-03-20', Resource='Not Started'),
#      dict(Task="Job-3", Start='2017-04-01', Finish='2017-04-20', Resource='Not Started'),
#      dict(Task="Job-3", Start='2017-05-18', Finish='2017-06-18', Resource='Not Started'),
#      dict(Task="Job-4", Start='2017-01-14', Finish='2017-03-14', Resource='Complete')]
