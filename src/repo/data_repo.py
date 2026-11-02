from abc import ABC, abstractmethod

import pandas as pd

from src.constants import (
    BankCategory,
    DonationCategory,
    DonationEvent,
    DonorType,
    ExpenseCategory,
)


class DataRepo(ABC):
    """Container for fetch data methods."""

    @abstractmethod
    def get_bank_data(_self, category: BankCategory | None) -> pd.DataFrame:
        """Gets bank account items or all if no filters are provided."""
        raise NotImplementedError()

    @abstractmethod
    def get_contributions_data(
        _self,
        donor_type: DonorType | None = None,
        category: DonationCategory | None = None,
        event: DonationEvent | tuple[DonationEvent] = (),
    ) -> pd.DataFrame:
        """Gets contribution items or all if no filters are provided."""
        raise NotImplementedError()

    @abstractmethod
    def get_loans_data(_self, names: tuple[str] = ()) -> pd.DataFrame:
        """Gets loan items or all if no filters are provided."""
        raise NotImplementedError()

    @abstractmethod
    def fetch_expenses_data(_self) -> pd.DataFrame:
        """Gets the raw expenses data."""
        raise NotImplementedError()

    def filter_expenses_data(_self, category: ExpenseCategory) -> pd.DataFrame:
        """Gets the expenses data by category."""
        df_raw = _self.fetch_expenses_data().query("category == @category")

        return df_raw.reset_index(drop=True).drop(columns="category")

    @abstractmethod
    def get_members_data(_self) -> pd.DataFrame:
        pass
