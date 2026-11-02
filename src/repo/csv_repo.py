from typing import override

import pandas as pd
import streamlit as st

from src.constants import BankCategory, DonationCategory, DonationEvent, DonorType
from src.repo.data_repo import DataRepo


class CsvRepo(DataRepo):
    """Container for fetch data methods."""

    @st.cache_data(hash_funcs={BankCategory: lambda c: c.value})
    @override
    def get_bank_data(_self, category: BankCategory | None) -> pd.DataFrame:
        """Gets bank account items or all if no filters are provided."""

        df_raw = pd.read_csv(
            "data/bank.csv", parse_dates=["date"], date_format="%y-%m-%d"
        )

        df_raw["net"] = df_raw["interest"] - df_raw["tax"]

        if not category:
            return df_raw

        return df_raw.query("category == @category")

    @st.cache_data(
        hash_funcs={
            DonorType: lambda t: t.value,
            DonationCategory: lambda c: c.value,
            DonationEvent: lambda e: e.value,
        }
    )
    @override
    def get_contributions_data(
        _self,
        donor_type: DonorType | None = None,
        category: DonationCategory | None = None,
        event: DonationEvent | tuple[DonationEvent] = (),
    ) -> pd.DataFrame:
        """Returns the rows matching the query, else returns all if no filters is passed."""
        df_raw = pd.read_csv(
            "data/contributions.csv", parse_dates=["date"], date_format="%y-%m-%d"
        )

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

    @st.cache_data()
    @override
    def get_loans_data(_self, names: tuple[str] = ()) -> pd.DataFrame:
        """Gets loan items or all if no filters are provided."""
        df_raw = pd.read_csv(
            "data/loans.csv", parse_dates=["date"], date_format="%y-%m-%d"
        )

        if names:
            return df_raw.query("name in @names")

        return df_raw

    @override
    def get_expenses_data(_self) -> pd.DataFrame:
        pass

    @override
    def get_members_data(_self) -> pd.DataFrame:
        pass
