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
    df['CR'] = df['CR'].astype('string')
    
    orders = list(df['CR'])
    
    st.write(df)
    
#ACTION
#    st.to_csv(s3_string+dt_string)

    fig = px.timeline(df
                      , x_start="Start"
                      , x_end="Finish"
                      , y="CR"
                      , hover_name="Task"
                      , color='Status'
                      , opacity=.7
    )
    
    fig.update_yaxes(autorange="reversed")     
    
    fig
    
