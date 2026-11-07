from typing import override

import pandas as pd
import streamlit as st

from src.repo.data_repo import DataRepo


class CsvRepo(DataRepo):
    """Container for fetch data methods."""

    def _load_csv(_self, filepath: str, date_col: str = "date") -> pd.DataFrame:
        """Internal helper to load csv with parsed dates."""
        df_raw = pd.read_csv(filepath, parse_dates=[date_col], date_format="%Y-%m-%d")
        df_raw[date_col] = df_raw[date_col].dt.date
        return df_raw

    @st.cache_data
    @override
    def fetch_bank_data(_self) -> pd.DataFrame:
        """Gets the entire cached Bank table with Net computed."""
        df_raw = _self._load_csv("data/bank.csv")
        df_raw["net"] = df_raw["interest"] - df_raw["tax"]
        return df_raw

    @st.cache_data
    @override
    def fetch_contributions_data(_self) -> pd.DataFrame:
        """Gets the entire cached Contributions table."""
        return _self._load_csv("data/contributions.csv")

    @st.cache_data
    @override
    def fetch_loans_data(_self) -> pd.DataFrame:
        """Gets the entire cached Loans table."""
        return _self._load_csv("data/loans.csv")

    @st.cache_data
    @override
    def fetch_expenses_data(_self) -> pd.DataFrame:
        """Gets the entire cached Expenses table."""
        return _self._load_csv("data/expenses.csv")

    @st.cache_data
    @override
    def fetch_members_data(_self) -> pd.DataFrame:
        """Gets the entire cached Members table."""
        return _self.read_csv("data/members.csv", date_col="appointment_date")
