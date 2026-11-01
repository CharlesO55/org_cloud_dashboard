from abc import ABC, abstractmethod
import pandas as pd
from src.constants import ExpenseCategory


class DataRepo(ABC):
    """Container for fetch data methods."""

    @abstractmethod
    def get_savings_data(_self) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_individual_contributions_data(_self) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_loans_data(_self) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_expenses_data(_self, categories: list[ExpenseCategory]) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_members_data(_self) -> pd.DataFrame:
        pass
