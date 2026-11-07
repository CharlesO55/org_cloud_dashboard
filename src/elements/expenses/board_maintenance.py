import pandas as pd
import streamlit as st

from repo.clients import get_repo_client
from app_constants import ExpenseCategory


def board_maintenance():
    df = get_repo_client().filter_expenses_data(ExpenseCategory.MAINTENANCE)

    with st.container(border=1):
        st.subheader("Metrics")
        _maintenance_metrics(df)

    with st.container(border=1):
        st.subheader("Monthly Utilities")
        _maintenance_timeline(df)

    with st.container(border=1):
        st.subheader("Records")
        _maintenance_table(df)


def _maintenance_metrics(df: pd.DataFrame):
    df_avg = (
        df.query(f"item in {('电', '水')}")[["item", "amount"]]
        .groupby("item", as_index=True)
        .mean()
    )

    cols = st.columns(3)

    with cols[0]:
        st.metric("Total", df["amount"].sum(), format="%,d")

    with cols[1]:
        st.metric("Electricity Avg", df_avg.loc["电"], format="%,d")

    with cols[2]:
        st.metric("Water Avg", df_avg.loc["水"], format="%,d")


def _maintenance_timeline(df: pd.DataFrame):
    df_timeline = df.query(f"item in {('电', '水')}")[["date", "item", "amount"]]
    st.line_chart(df_timeline, x="date", y="amount", color="item")


def _maintenance_table(df: pd.DataFrame):
    st.dataframe(
        df,
        column_config={"amount": st.column_config.NumberColumn(format="%,d")},
    )
