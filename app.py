# Import libraries
from ctypes import alignment
from select import select
import streamlit as st
import pandas as pd
import numpy as np
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from streamlit_option_menu import option_menu
import time
from datetime import datetime
import plotly.express as px
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from  PIL import Image
from plotly.graph_objs import *


def main():
################################# Set page layout ################################# 
    st.set_page_config(layout='wide') #Choose wide mode as the default setting
    st.markdown("<h1 style='text-align: center; color: black;'>Data Analytics App</h1>"
        """
        <style>
            [data-testid=stImage]{
                text-align: center;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }
        </style>
        """, unsafe_allow_html=True
    )
    st.image("images/img1.png", width=250)

################################# Set sidebar layout ################################# 
    st.markdown(
        """
        <style>
            [data-testid=stSidebar] [data-testid=stImage]{
                text-align: center;
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 100%;
            }
        </style>
        """, unsafe_allow_html=True
    )
    with st.sidebar: 
        st.sidebar.image('images/robot.png',  width=120)
        # st.title("")
        st.info("This web application helps to analyze and explore dataset.")

    # font_css = """
    # <style>
    # button[data-baseweb="tab"] {
    #   font-size: 2px;
    # }
    # </style>
    # """
    # st.write(font_css, unsafe_allow_html=True)

    ################################# Set multiple tabs ################################# 
    tab1, tab2, tab3, tab4 = st.tabs(["File", "Data Visualization", "Data profiling", 'Machine Learning'])

    ############################################ Tab 1: File ##########################################
    with tab1: 
        upload_file = st.file_uploader('upload your file', type='.csv')
        if upload_file:
            df = pd.read_csv(upload_file)
            option1=st.sidebar.radio(
            'Choose features for Analysis',
            ('All features', 'A subset of fearures'))
            if option1=='All features':
                df=df

            elif option1 == 'A subset of fearures':
                var_list=list(df.columns)
                option3=st.sidebar.multiselect(
                'Select variable(s) you want to include in the report.',var_list)
                df=df[option3]
                st.info("If error, please select column names on left side panel.")
                # for i in df:
                #     agree = st.sidebar.checkbox(i, key= i)
            
            st.header('Dataset:')
            st.dataframe(df,use_container_width=True)
            m = st.markdown("""
            <style>
            div.stButton > button:first-child {
                background-color: #0099ff;
                color:#ffffff;
            }
            </style>""", unsafe_allow_html=True)
            dwn_btn = st.button('Download dataset')
            if dwn_btn:
                df.to_csv('dataset_.csv')
                st.write('File has been downloaded!')

    ########################################### Tab 2: Data Visualization ###########################################
            with tab2:
                ############ set index ############
                df = df.set_index(df.columns[0])          
                ############ Line graph ############
                st.title('Plot')
                st.info('Line Plot')
                # fig1 = px.line(df.drop(['class'], axis=1))
                fig1 = px.line(df, title='Dataset')
                st.plotly_chart(fig1, use_container_width=True)

                # col1, col2 = st.columns(2)
                # with col1:
                #     ############ Bar graph ############
                #     val_count = df['class'].value_counts()
                #     st.info('Bar Graph:')
                #     fig2 = px.bar(val_count, title='Number of class samples')
                #     st.plotly_chart(fig2, use_container_width=True)
                    
                # with col2:
                #     ############ Pie graph ############
                #     st.info("Pie Chart")
                #     fig3 = px.pie(df, names='class', title='Percentage of class samples')
                #     st.plotly_chart(fig3, use_container_width=True)
                    
    ############################################ Tab 3: Data profiling ############################################
            with tab3:
                # st.title('Data Analysis')
                st.write(df.describe())
                st.title("Exploratory Data Analysis")
                profile_df = df.profile_report()
                gen = st.button('Generate Report', key = 2)
                if gen:
                    st_profile_report(profile_df)
                    
    ############################################ Tab 4: Machine Learning ############################################
                with tab4:
                    load_lib = st.button('Automate ML', key = 3)
                    
                    if load_lib:
                        # st.markdown('Import Machine Learning Libraries')
                        with st.spinner('Performing ML pipeline'):
                            st.success('Machine learning: Coming soon')

if __name__ == '__main__':
    main()