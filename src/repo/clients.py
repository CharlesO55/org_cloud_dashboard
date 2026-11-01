# Provide current active clients
import streamlit as st

from repo.data_repo import DataRepo
from repo.csv_repo import CsvRepo


@st.cache_resource
def get_repo_client() -> DataRepo:
    return CsvRepo()
