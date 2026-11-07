import pandas as pd
import streamlit as st

from src.repo.clients import get_repo_client


@st.cache_data
def load_old_balance():
    df = pd.read_csv("data/1_1 balance.csv", index_col=0)
    latest_year = df.index.max()

    return df.loc[latest_year]["金额"]


with st.spinner("Initializing..."):
    _client = get_repo_client()

with st.spinner("Loading charts..."):
    df_income = pd.Series(
        {
            "Contributions": _client.filter_contributions_data()["amount"].sum(),
            "Bank": _client.filter_bank_data()["net"].sum(),
            "Loans": _client.filter_loans_data()["amount"].sum(),
        }
    )

    df_expenses = _client.fetch_expenses_data().groupby("category")["amount"].sum() * -1

    total_income = df_income.sum()
    total_expenses = df_expenses.sum()

    latest_balance = load_old_balance()


with st.container(border=1):
    st.subheader("Summary")

    cols = st.columns(3)

    with cols[0]:
        st.metric("Previous Surplus", latest_balance, format="%,.2f")

    with cols[1]:
        st.metric("Total Income", total_income, format="%,.2f")

    with cols[2]:
        st.metric("Total Expenses", total_expenses, format="%,.2f")

    st.divider()
    st.metric(
        "Total Balance", latest_balance + total_income + total_expenses, format="%,.2f"
    )


with st.container(border=1):
    st.subheader("Income")

    st.dataframe(
        df_income,
        column_config={"0": st.column_config.NumberColumn("Amount", format="%,.2f")},
    )
    st.bar_chart(df_income, horizontal=True)


with st.container(border=1):
    st.subheader("Expenses")

    st.dataframe(
        df_expenses,
        column_config={
            "amount": st.column_config.NumberColumn("Amount", format="%,.2f")
        },
    )
    st.bar_chart(df_expenses.abs(), horizontal=True, color="#FF0000")
