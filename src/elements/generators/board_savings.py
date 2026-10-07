import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/1_5 savings.csv", parse_dates=['日期'], date_format='%m-%d-%y')
    df['日期'] = df['日期'].dt.date
    df['实收利息'] = df['利息'] + df['扣税']

    total_net_interest = df['实收利息'].sum()

    return df , total_net_interest

def board_savings():
    df , total_net_interest = load_data()

    with st.container(border=1):
        st.subheader("Metrics")

        st.metric("Total Net Interest", total_net_interest)

    with st.container(border=1):
        st.subheader("Monthly Net Interest")
        st.bar_chart(df, x='日期', y='实收利息')
    

    with st.container(border=1):
        st.subheader("Records")
        st.dataframe(df)
