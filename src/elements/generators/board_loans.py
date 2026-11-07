import pandas as pd
import streamlit as st

from repo.clients import get_repo_client


@st.cache_data
def _cache_unique_names():
    return get_repo_client().filter_loans_data()["name"].unique()


@st.fragment
def board_loans():
    with st.container(border=1):
        selected_names = st.multiselect(
            "Name", options=_cache_unique_names(), default=_cache_unique_names()
        )

        df_raw = get_repo_client().filter_loans_data(
            tuple(selected_names) if selected_names else ()
        )

        _loan_metrics(df_raw)
        _monthly_timeline(df_raw)
        _loans_table(df_raw)


def _loan_metrics(df: pd.DataFrame):
    cols = st.columns(2)

    with cols[0]:
        st.metric("Total", value=df["amount"].sum(), format="%,d")

    with cols[1]:
        st.metric("Repayments", value=df["amount"].count(), format="%,d")


def _monthly_timeline(df: pd.DataFrame):
    st.bar_chart(df, x="date", y="amount", color="name")


def _loans_table(df: pd.DataFrame):
    return st.dataframe(
        df, column_config={"amount": st.column_config.NumberColumn(format="%,d")}
    )
