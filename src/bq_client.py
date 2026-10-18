from google.cloud import bigquery
import pandas as pd
import streamlit as st

from src.constants import TableNames


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
            FROM `{TableNames.savings}`
        """
        return _self._get_data(query_string)

    @st.cache_data
    def get_individual_contributions_data(_self) -> pd.DataFrame:
        query_string = f"""
            SELECT *
            FROM `{TableNames.contributions}`
            WHERE donor_type='member'
                AND category IN ('raffle','hospitality','donation')
                AND event IS NULL
            ORDER BY date, amount
        """
        return _self._get_data(query_string)


if __name__ == "__main__":
    repo = DataRepo()
    df = repo.get_savings_data()
    print(df)

    df = repo.get_individual_contributions_data()
    print(df)
