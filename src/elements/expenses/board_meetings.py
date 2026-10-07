import pandas as pd
import streamlit as st


def load_data():
    df_raw = pd.read_csv("data/2_3 monthly meetings.csv", parse_dates=['日期'], date_format='%m-%d-%y').sort_values('日期').reset_index(drop=True)
    df_raw['日期'] = df_raw['日期'].dt.date

    return df_raw 

def board_meetings():
    df_raw = load_data()
    
    with st.container(border=1):
        st.subheader("Metrics")
        st.metric('Total Expenses', df_raw['金额'].sum(), format="%,d")
        
        
    with st.container(border=1):
        st.subheader("Timeline")
        
        st.bar_chart(df_raw.groupby("日期").sum(), y='金额', color="#FF0000")

    with st.container(border=1):
        st.subheader("Records")
        st.dataframe(df_raw, column_config={
            "金额" : st.column_config.NumberColumn(format="%,d")
        })