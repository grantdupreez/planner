import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

#set the plan logging
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%Y%m%d%H%M%S")+".csv"

s3_string = ""
#S3 storage for the plan logging

#ACTION activate this when the log location is known - st.write('S3 path and log filename: '+s3_string+dt_string)


st.write("**Upload project plan for a Gantt chart view**")
st.write("Use the template csv file")

uploaded_file = st.sidebar.file_uploader("Choose a file",type=['CSV'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, header=[0], encoding='latin1')
    
#    df['Start'] = pd.to_datetime(df['Start'])

    df['Start'] = df['Start'].astype('datetime64')
    df['Finish'] = df['Finish'].astype('datetime64')
    
#    orders = list(df['CR'])
    
    st.write(df)
    
#ACTION
#    st.to_csv(s3_string+dt_string)
    
#    fig = ff.create_gantt(df, index_col='Status', show_colorbar=True,
#                         showgrid_x=True, showgrid_y=True)
 
    colors = {'Not Started': 'rgb(220, 0, 0)'
              , 'Incomplete': (1, 0.9, 0.16)
              , 'Complete': 'rgb(0, 255, 100)'}
    
    fig = px.timeline(df
                      , x_start="Start"
                      , x_end="Finish"
                      , y="CR"
                      , hover_name="Task"
                      , color=colors
                      , index_col='Status'
                      , show_colorbar=True,
 #                     , range_x=None
 #                     , range_y=None
                      , opacity=.7
                      
    )
     
    fig
    
