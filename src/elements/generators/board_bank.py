import pandas as pd
import streamlit as st

from app_constants import BankCategory
from repo.clients import get_repo_client


@st.fragment
def board_bank():
    with st.container(border=1):
        selected_bank_category = st.segmented_control(
            "Category", options=list(BankCategory)
        )

        df = get_repo_client().filter_bank_data(category=selected_bank_category)

        _total_metrics(df)
        _monthly_interest_timeline(df)
        _transactions_table(df, selected_bank_category)


def _total_metrics(df: pd.DataFrame):
    df_sums = df[["category", "net"]].groupby("category", as_index=False).sum()

    cols = st.columns(2)
    for i, row in enumerate(df_sums.itertuples()):
        with cols[i]:
            st.metric(label=row.category, value=row.net, format="%,d")


def _monthly_interest_timeline(df: pd.DataFrame):
    df_agg = (
        df.copy()[["date", "category", "net"]]
        .assign(date=lambda df: pd.to_datetime(df["date"]).dt.to_period("M"))
        .groupby(["date", "category"], as_index=False)["net"]
        .sum()
    )

    df_agg["date"] = df_agg["date"].astype(str)

    st.subheader("Monthly Net Income")
    st.bar_chart(df_agg, x="date", y="net")


def _transactions_table(df: pd.DataFrame, category: BankCategory):
    cols = (
        ["account", "date", "interest", "tax"]
        if category != BankCategory.INTEREST
        else ["date", "interest", "tax"]
    )

    st.dataframe(
        df[cols],
        column_config={
            "interest": st.column_config.NumberColumn(format="%,.2f"),
            "tax": st.column_config.NumberColumn(format="%,.2f"),
        },
    )
