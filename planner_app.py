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
    
    df['Start'] = pd.to_datetime(df['Start'])

    df['Start'] = df['Start'].astype('datetime64')
    df['Finish'] = df['Finish'].astype('datetime64')
    
#    orders = list(df['Task'])
    
    st.write(df)
    
#ACTION
#    st.to_csv(s3_string+dt_string)
    
#    fig = ff.create_gantt(df, index_col='Status', show_colorbar=True,
#                         showgrid_x=True, showgrid_y=True)
 
    
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", hover_name="Task",
                     color_discrete_sequence=px.colors.qualitative.Prism
                  , opacity=.7
                     , range_x=None
                  , range_y=None
                  , template='plotly_white'
                  , height=1200
                     , color='Task'
                  , title ="<b>IE 3.0 Gantt Chart 2021</b>"
    )
    
    fig.update_layout(
        bargap=0.5
        ,bargroupgap=0.1
        ,xaxis_range=[df.Start.min(), df.Finish.max()]
        ,showgrid=True
        ,rangeslider_visible=True
        ,side ="top"
        ,tickmode = 'array'
        ,dtick="M1"
        ,tickformat="Q%q %Y \n"
        ,ticklabelmode="period"        
        ,ticks="outside"
        ,tickson="boundaries"
        ,tickwidth=.1
        ,layer='below traces'
        ,ticklen=20
        ,tickfont=dict(
            family='Old Standard TT, serif',size=24,color='gray')
        ,rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
            ,x=.37
            ,y=-.05
            ,font=dict(
                family="Arial",
                size=14,
                color="darkgray"
        )))
        ,yaxis = dict(
            title= ""
            ,autorange="reversed"
            ,automargin=True
            ,ticklen=10
            ,showgrid=True
            ,showticklabels=True
            ,tickfont=dict(
                family='Old Standard TT, serif', size=16, color='gray'))

        ,legend=dict(
            orientation="h"
            ,yanchor="bottom"
            ,y=1.1
            ,title=""
            ,xanchor="right"
            ,x=1
            ,font=dict(
                family="Arial"
                ,size=14
                ,color="darkgray"))
        )
    )
        
        
    fig.update_traces(marker_line_color='rgb(8,48,107)'
        , marker_line_width=1.5, opacity=0.95)
                          
    fig.update_layout(
            title="<b>IE 3.0 Gantt Chart 2021</b>",
            xaxis_title="",
            yaxis_title="Initiatives",
            font=dict(
                family="Arial",
                size=24,
                color="darkgray"
            )
        )
 
    fig
    
    go.FigureWidget(fig)
