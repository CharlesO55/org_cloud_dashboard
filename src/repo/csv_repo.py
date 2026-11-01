from typing import override

import pandas as pd
import streamlit as st

from src.constants import DonorType
from src.repo.data_repo import DataRepo


class CsvRepo(DataRepo):
    """Container for fetch data methods."""

    @override
    def get_savings_data(_self) -> pd.DataFrame:
        pass

    @override
    def get_individual_contributions_data(_self) -> pd.DataFrame:
        df_raw = pd.read_csv("data/contributions.csv")
        return df_raw.query(f"donor_type == '{DonorType.INDIVIDUAL}'").reset_index()

    @st.cache_data
    @override
    def get_organization_contributions_data(_self) -> pd.DataFrame:
        df_raw = pd.read_csv("data/contributions.csv")
        return df_raw.query(f"donor_type == '{DonorType.ORGANIZATION}'").reset_index()

    @override
    def get_loans_data(_self) -> pd.DataFrame:
        pass

    @override
    def get_expenses_data(_self) -> pd.DataFrame:
        pass

    @override
    def get_members_data(_self) -> pd.DataFrame:
        pass
