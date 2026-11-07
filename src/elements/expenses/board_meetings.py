import streamlit as st

from repo.clients import get_repo_client
from app_constants import ExpenseCategory


def board_meetings():
    df = get_repo_client().filter_expenses_data(ExpenseCategory.MEETINGS)

    with st.container(border=1):
        st.subheader("Metrics")
        st.metric("Total", df["amount"].sum(), format="%,d")

    with st.container(border=1):
        st.subheader("Timeline")
        st.bar_chart(df.groupby("date").sum(), y="amount", color="#FF0000")

    with st.container(border=1):
        st.subheader("Records")
        st.dataframe(
            df, column_config={"amount": st.column_config.NumberColumn(format="%,d")}
        )
