import streamlit as st
import pandas as pd
import plotly.figure_factory as ff

#set the plan logging
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%Y%m%d%H%M%S")+".csv"

s3_string = ""
#S3 storage for the plan logging
st.write('S3 path and log filename: '+s3_string+dt_string)


st.write("**Upload project plan for a Gantt chart view**")
st.write("Use the template csv file")

uploaded_file = st.sidebar.file_uploader("Choose a file",type=['CSV'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, header=[0], parse_dates=[1])
    st.write(df)
    
#    st.to_csv(dt_string + '.csv')
    
    fig = ff.create_gantt(df, index_col='Status', show_colorbar=True,
                         showgrid_x=True, showgrid_y=True)
 
    fig
    
