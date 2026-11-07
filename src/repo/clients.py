# Provide current active clients
import streamlit as st

from repo.bq_repo import BigqueryRepo
from repo.data_repo import DataRepo


@st.cache_resource
def get_repo_client() -> DataRepo:
    return BigqueryRepo()
