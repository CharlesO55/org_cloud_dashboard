from typing import override

import pandas as pd
import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account

from src.constants import TableName
from src.repo.data_repo import DataRepo


class BigqueryRepo(DataRepo):
    def __init__(self):
        credentials = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"]
        )
        self._client = bigquery.Client(
            credentials=credentials, project=credentials.project_id
        )

    def _run_query(_self, sql: str) -> pd.DataFrame:
        return _self._client.query(query=sql).to_dataframe()

    @st.cache_data
    @override
    def fetch_bank_data(_self) -> pd.DataFrame:
        """Gets the entire cached Bank table with Net computed."""
        query_string = f"""
            SELECT *, 
                (IFNULL(interest, 0) - IFNULL(tax, 0)) AS net
            FROM `{TableName.Bank}`
            ORDER BY date DESC
        """
        return _self._run_query(query_string)

    @st.cache_data
    @override
    def fetch_contributions_data(_self) -> pd.DataFrame:
        """Gets the entire cached Contributions table."""

        query_string = f"""
            SELECT *
            FROM `{TableName.Contributions}`
            ORDER BY date DESC, amount DESC
        """
        return _self._run_query(query_string)

    @st.cache_data
    @override
    def fetch_loans_data(_self) -> pd.DataFrame:
        """Gets the entire cached Loans table."""
        query_string = f"""
            SELECT *
            FROM `{TableName.Loans}`
            ORDER BY date DESC, amount DESC
        """
        return _self._run_query(query_string)

    @st.cache_data
    def fetch_expenses_data(_self) -> pd.DataFrame:
        query_string = f"""
            SELECT *
            FROM `{TableName.Expenses}`
            ORDER BY date DESC, amount DESC
        """
        return _self._run_query(query_string)

    @st.cache_data
    @override
    def fetch_members_data(_self) -> pd.DataFrame:
        """Gets the entire cached Members table."""
        query_string = f"""
            SELECT *
            FROM `{TableName.Members}`
            ORDER BY appointment_date DESC
        """
        return _self._run_query(query_string)
