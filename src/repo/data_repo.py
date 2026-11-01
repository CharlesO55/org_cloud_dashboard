from abc import ABC, abstractmethod
import pandas as pd


class DataRepo(ABC):
    """Container for fetch data methods."""

    @abstractmethod
    def get_savings_data(_self) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_contributions_data(
        _self,
        donor_type: str | None = None,
        category: str | None = None,
        event: str | tuple[str] = (),
    ) -> pd.DataFrame:
        pass

    def get_contributions_agg(
        _self,
    ) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_loans_data(_self) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_expenses_data(_self) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_members_data(_self) -> pd.DataFrame:
        pass
