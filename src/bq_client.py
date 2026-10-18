import pandas as pd
import streamlit as st
from google.cloud import bigquery

from src.constants import ExpenseCategory, TableName


@st.cache_resource
def get_bq_client() -> bigquery.Client:
    return bigquery.Client(
        project=st.secrets["project_id"],
        location=st.secrets["location"],
    )


class DataRepo:
    """Container for fetch data methods."""

    def __init__(self):
        pass

    def _get_data(self, sql: str) -> pd.DataFrame:
        return get_bq_client().query(query=sql).to_dataframe()

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


if __name__ == "__main__":
    repo = DataRepo()
    df = repo.get_expenses_data([ExpenseCategory.Maintenance, ExpenseCategory.Meetings])
    print(df)
