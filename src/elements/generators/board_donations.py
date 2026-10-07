import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    df = pd.read_csv("data/1_2 donations.csv")
    df_summary = df[["捐", "抽奖", "招待"]].sum()

    old_balance = df[df["捐贈者"] == "会所餘"]['捐'].sum()

    return df, df_summary, old_balance


def board_dontations():
    df, df_summary, old_balance = load_data()

    with st.container(border=1):
        st.subheader("Metrics")
        cols = st.columns(3)
        with cols[0]:
            st.metric("捐 Total", 
                value=df_summary["捐"], 
                delta=df_summary["捐"]-old_balance,
                format="%,d"
            )

        with cols[1]:
            st.metric("抽奖 Total", df_summary["抽奖"], format="%,d")

        with cols[2]:
            st.metric("招待 Total", df_summary["招待"], format="%,d")



    with st.container(border=1):
        st.subheader("Records")
        col_config = {
            "捐" : st.column_config.NumberColumn(format="%,d"),
            "抽奖" : st.column_config.NumberColumn(format="%,d"),
            "招待" : st.column_config.NumberColumn(format="%,d"),
        }
        st.dataframe(df, column_config=col_config)