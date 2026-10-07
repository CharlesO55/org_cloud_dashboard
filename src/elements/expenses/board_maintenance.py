import pandas as pd
import streamlit as st


def load_data():
    df_raw = pd.read_csv("data/2_5 maintenance expenses.csv", parse_dates=['日期'], date_format='%m-%d-%y').sort_values('日期').reset_index(drop=True)
    df_raw['日期'] = df_raw['日期'].dt.date
    df_utilities = df_raw[df_raw['明细'].isin(['电','水'])]

    return df_raw , df_utilities

def board_maintenance():
    df_raw , df_utilities= load_data()
    
    with st.container(border=1):
        st.subheader("Metrics")

        cols = st.columns(3)

        with cols[0]:
            st.metric('Total Expenses', df_raw['金额'].sum(), format="%,d")
        with cols[1]:
            st.metric('Eletricity avg', df_utilities[df_utilities['明细'] == '电']['金额'].mean(), format="%,d")
        with cols[2]:
            st.metric('Water avg', df_utilities[df_utilities['明细'] == '水']['金额'].mean(), format="%,d")

    with st.container(border=1):
        st.subheader("Monthly Utilities")
        st.line_chart(df_utilities, x="日期", color='明细', y='金额', )

    with st.container(border=1):
        st.subheader("Records")
        st.dataframe(df_raw, column_config={
            "金额" : st.column_config.NumberColumn(format="%,d")
        })