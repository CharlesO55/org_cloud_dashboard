import pandas as pd
import streamlit as st

from app_constants import DonationCategory
from repo.clients import get_repo_client

with st.spinner("Initializing..."):
    _client = get_repo_client()

with st.spinner("Loading charts..."):
    total_contributions = _client.filter_contributions_data(
        category=[
            DonationCategory.DONATION,
            DonationCategory.HOSPITALITY,
            DonationCategory.RAFFLE,
        ]
    )["amount"].sum()

    prev_surplus = _client.filter_contributions_data(
        category=[DonationCategory.SURPLUS]
    )["amount"].sum()

    df_income = pd.Series(
        {
            "Contributions": total_contributions,
            "Bank": _client.filter_bank_data()["net"].sum(),
            "Loans": _client.filter_loans_data()["amount"].sum(),
        }
    )

    df_expenses = _client.fetch_expenses_data().groupby("category")["amount"].sum() * -1
    df_expenses.index = df_expenses.index.str.title()

    total_income = df_income.sum()
    total_expenses = df_expenses.sum()


with st.container(border=1):
    st.subheader("Summary")

    cols = st.columns(3)

    with cols[0]:
        st.metric("Previous Surplus", prev_surplus, format="%,.2f")

    with cols[1]:
        st.metric("Total Income", total_income, format="%,.2f")

    with cols[2]:
        st.metric("Total Expenses", total_expenses, format="%,.2f")

    st.divider()
    st.metric(
        "Outstanding Balance",
        value=prev_surplus + total_income + total_expenses,
        delta=total_income + total_expenses,
        format="%,.2f",
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
            "category": st.column_config.TextColumn("category"),
            "amount": st.column_config.NumberColumn("Amount", format="%,.2f"),
        },
    )
    st.bar_chart(df_expenses.abs(), horizontal=True, color="#FF0000")
