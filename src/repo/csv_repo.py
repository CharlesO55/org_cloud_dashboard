from typing import override

import pandas as pd
import streamlit as st

from src.repo.data_repo import DataRepo


class CsvRepo(DataRepo):
    """Container for fetch data methods."""

    @override
    def get_savings_data(_self) -> pd.DataFrame:
        pass

    @st.cache_data
    @override
    def get_contributions_data(
        _self,
        donor_type: str | None = None,
        category: str | None = None,
        event: str | tuple[str] = (),
    ) -> pd.DataFrame:
        """Returns the rows matching the query, else returns all if no filters is passed."""
        df_raw = pd.read_csv("data/contributions.csv")

        conditions = []
        if donor_type:
            conditions.append("donor_type == @donor_type")
        if category:
            conditions.append("category == @category")
        if event:
            conditions.append("event in @event")

        if conditions:
            query_str = " and ".join(conditions)
            return df_raw.query(query_str).reset_index(drop=True)

        return df_raw.reset_index(drop=True)

    @st.cache_data
    @override
    def get_contributions_agg(
        _self,
    ) -> pd.DataFrame:
        """Returns the rows matching the query, else returns all if no filters is passed."""

        df = _self.get_contributions_data()

        df_agg = (
            df[["donor_type", "category", "amount"]]
            .groupby(["donor_type", "category"], as_index=False)
            .sum()
        )

        return df_agg

    @override
    def get_loans_data(_self) -> pd.DataFrame:
        pass

    @override
    def get_expenses_data(_self) -> pd.DataFrame:
        pass

    @override
    def get_members_data(_self) -> pd.DataFrame:
        pass
