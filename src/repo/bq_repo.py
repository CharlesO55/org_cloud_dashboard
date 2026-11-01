import pandas as pd
import streamlit as st
from google.cloud import bigquery

from src.constants import ExpenseCategory, TableName

from src.data_repo import DataRepo


class BigqueryRepo(DataRepo):
    def __init__(self):
        self.client = bigquery.Client(
            project=st.secrets["project_id"],
            location=st.secrets["location"],
        )

    def _get_data(self, sql: str) -> pd.DataFrame:
        return self.client.query(query=sql).to_dataframe()

    @st.cache_data
    def get_savings_data(_self) -> pd.DataFrame:
        query_string = f"""
            SELECT *
            FROM `{TableName.Savings}`
        """
        return _self._get_data(query_string)

    @st.cache_data
    def get_individual_contributions_data(_self) -> pd.DataFrame:
        query_string = f"""
            SELECT *
            FROM `{TableName.Contributions}`
            WHERE donor_type='member'
                AND category IN ('raffle','hospitality','donation')
                AND event IS NULL
            ORDER BY date, amount
        """
        return _self._get_data(query_string)

    @st.cache_data
    def get_loans_data(_self) -> pd.DataFrame:
        query_string = f"""
            SELECT *
            FROM `{TableName.Loans}`
        """
        return _self._get_data(query_string)

    @st.cache_data
    def get_expenses_data(_self, categories: list[ExpenseCategory]) -> pd.DataFrame:
        categories_arr = [cat.value for cat in categories]

        query_string = f"""
            SELECT *
            FROM `{TableName.Expenses}`
            WHERE category IN UNNEST({categories_arr})
        """
        print(query_string)
        return _self._get_data(query_string)

    @st.cache_data
    def get_members_data(_self) -> pd.DataFrame:
        query_string = f"""
            SELECT *
            FROM `{TableName.Members}`
        """
        return _self._get_data(query_string)
