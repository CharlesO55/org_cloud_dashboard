import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    df_raw = pd.read_csv("data/1_3 org donations.csv")
    total_donations = df_raw['捐'].sum()

    return df_raw , total_donations

def board_org_dontations():
    df_raw , total_donations = load_data()

    with st.container(border=1):
        st.subheader("Metrics")
        st.metric(label="捐 Total", value=total_donations, format="%,d")


    with st.container(border=1):
        st.subheader("Records")
        st.dataframe(df_raw, column_config={
            "捐" : st.column_config.NumberColumn(format="%,d"),
        }
)