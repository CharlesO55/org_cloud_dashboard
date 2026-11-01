from src.repo.data_repo import DataRepo
from typing import override
import pandas as pd

from src.constants import ExpenseCategory


class CsvRepo(DataRepo):
    """Container for fetch data methods."""

    @override
    def get_savings_data(_self) -> pd.DataFrame:
        pass

    @override
    def get_individual_contributions_data(_self) -> pd.DataFrame:
        pass

    @override
    def get_loans_data(_self) -> pd.DataFrame:
        pass

    @override
    def get_expenses_data(_self, categories: list[ExpenseCategory]) -> pd.DataFrame:
        pass

    @override
    def get_members_data(_self) -> pd.DataFrame:
        pass
