import pandas as pd
import streamlit as st


def load_data():
    df_raw = pd.read_csv("data/2_1 ceremonies.csv", parse_dates=['日期'], date_format='%m-%d-%y').sort_values(['日期']).reset_index(drop=True)
    df_raw['日期'] = df_raw['日期'].dt.date

    return df_raw 

def board_ceremonies():
    df_raw = load_data()
    
    with st.container(border=1):
        st.subheader("Metrics")

        cols = st.columns(3)

        with cols[0]:
            st.metric('Total Expenses', df_raw['金额'].sum(), format="%,d")
        
        
    with st.container(border=1):
        st.subheader("Categorized")
        
        df_summary = df_raw.groupby('分类')['金额'].sum()
        st.bar_chart(df_summary, y='金额', color="#FF0000")

        st.dataframe(df_summary, column_config={
            "金额" : st.column_config.NumberColumn(format="%,d")
        })

    with st.container(border=1):
        st.subheader("Records")
        st.dataframe(df_raw, column_config={
            "金额" : st.column_config.NumberColumn(format="%,d")
        })