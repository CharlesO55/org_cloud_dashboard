import pandas as pd
import streamlit as st

from constants import DonationCategory, DonorType, DonationEvent
from repo.clients import get_repo_client


@st.fragment
def board_contributions():
    with st.container(border=1):
        _aggregate_cards()

        grid = [
            st.columns(2),
            st.columns(2),
        ]

        with grid[0][0]:
            selected_donor = st.segmented_control(
                "Donor Type",
                options=list(DonorType),
                default=DonorType.MEMBER,
                key="contribution_donor_type",
            )

        with grid[0][1]:
            selected_category = st.segmented_control(
                "Donation Category",
                options=list(DonationCategory),
                default=DonationCategory.DONATION,
                key="contribution_donation_category",
            )

        with grid[1][0]:
            selected_event = st.multiselect(
                "Event",
                options=list(DonationEvent),
                key="contribution_donation_event",
            )

        df = get_repo_client().get_contributions_data(
            donor_type=selected_donor,
            category=selected_category,
            event=tuple(selected_event) if selected_event else (),
        )

        _contribution_table(df)


def _aggregate_cards() -> None:
    df_agg = get_repo_client().get_contributions_agg()

    def render_donor_metrics(df, donor_type, title):
        st.subheader(title)
        filtered_df = df.query("donor_type == @donor_type")

        if filtered_df.empty:
            st.caption(f"No {title.lower()} data available.")
            return

        cols = st.columns(3)

        for i, row in enumerate(filtered_df.itertuples()):
            with cols[i % 3]:
                st.metric(label=row.category.title(), value=row.amount, format="%,d")

    render_donor_metrics(df_agg, DonorType.MEMBER, "Members")
    render_donor_metrics(df_agg, DonorType.ORGANIZATION, "Organizations")


def _contribution_table(df: pd.DataFrame) -> None:
    st.dataframe(
        df[["date", "donor_name", "amount"]],
        column_config={
            "amount": st.column_config.NumberColumn(format="%,d"),
        },
    )
