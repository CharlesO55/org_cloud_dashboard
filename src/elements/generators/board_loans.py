import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    df_raw = pd.read_csv("data/1_6 loans.csv", parse_dates=['日期'], date_format='%m-%d-%y')
    df_raw['月份'] = df_raw['日期'].dt.strftime('%Y-%m')
    df_raw['日期'] = df_raw['日期'].dt.date

    df_monthly = df_raw.groupby(['月份', '姓名'], as_index=False)['金额'].sum()

    df_summary = df_raw.groupby('姓名').aggregate(
        总金额=('金额', 'sum'),    
        笔数=('金额', 'count'),
        最后还款日=('日期', 'max')
    )

    return df_raw, df_monthly, df_summary


def board_loans():
    df_raw, df_monthly, df_summary = load_data()

    with st.container(border=1):
        st.subheader("Metrics")
        st.metric('Total Payments', df_monthly['金额'].sum(), format="%,d")


    with st.container(border=1):
        st.subheader("Monthly Payments")
        st.bar_chart(df_monthly, x='月份', y='金额', color='姓名')


    with st.container(border=1):
        st.subheader("Summary")
        
        st.dataframe(df_summary, column_config={
            '总金额' : st.column_config.NumberColumn(format="%,d")
        })

    

    with st.container(border=1):
        st.subheader("Records")

        col_config = {
            "金额" : st.column_config.NumberColumn(format="%,d")
        }
        st.dataframe(df_raw.drop(columns=['月份']), column_config=col_config)
