import pandas as pd
import streamlit as st

from constants import DonationCategory
from repo.clients import get_repo_client


@st.cache_data
def _cache_aggregate_data(df) -> pd.DataFrame:
    return df[["category", "amount"]].groupby("category", as_index=False).sum()


@st.cache_data
def _cache_filtered_data(df, category: str) -> pd.DataFrame:
    return df.query(f"category == '{category}'")[["date", "donor_name", "amount"]]


def board_org_dontations():
    df = get_repo_client().get_organization_contributions_data()

    with st.container(border=1):
        _aggregate_cards(df)
        _contribution_table(df)


def _aggregate_cards(df) -> None:
    df_agg = _cache_aggregate_data(df)

    st.subheader("捐")

    cols = st.columns(3)
    for row in df_agg.itertuples():
        with st.container(), cols[row.Index]:
            st.metric(label=row.category.title(), value=row.amount, format="%,d")


@st.fragment
def _contribution_table(df) -> None:

    selected_category = st.segmented_control(
        "Donation Category",
        options=list(DonationCategory),
        default=DonationCategory.DONATION,
        key="contribution_org_category",
    )

    df_filtered = _cache_filtered_data(df, selected_category)

    st.dataframe(
        df_filtered,
        column_config={
            "amount": st.column_config.NumberColumn(format="%,d"),
        },
    )
