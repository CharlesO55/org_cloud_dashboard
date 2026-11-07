from abc import ABC, abstractmethod

import pandas as pd

from app_constants import (
    BankCategory,
    DonationCategory,
    DonationEvent,
    DonorType,
    ExpenseCategory,
)


class DataRepo(ABC):
    """Container for fetch data methods."""

    @abstractmethod
    def fetch_bank_data(_self) -> pd.DataFrame:
        """Gets the entire cached Bank table with Net computed."""
        raise NotImplementedError()

    def filter_bank_data(_self, category: BankCategory | None = None) -> pd.DataFrame:
        """Gets bank account items or all if no filters are provided."""
        df_raw = _self.fetch_bank_data()

        if not category:
            return df_raw

        return df_raw.query("category == @category")

    @abstractmethod
    def fetch_contributions_data():
        """Gets the entire cached Contributions table."""
        raise NotImplementedError()

    def filter_contributions_data(
        _self,
        donor_type: DonorType | None = None,
        category: DonationCategory | None = None,
        event: DonationEvent | tuple[DonationEvent] = (),
    ) -> pd.DataFrame:
        """Gets contribution items or all if no filters are provided."""
        df_raw = _self.fetch_contributions_data()
        conditions = []
        if donor_type:
            conditions.append("donor_type == @donor_type")
        if category:
            conditions.append("category == @category")
        if event:
            conditions.append("event in @event")

        if conditions:
            query_str = " and ".join(conditions)
            return df_raw.query(query_str).reset_index(drop=True)

        return df_raw.reset_index(drop=True)

    @abstractmethod
    def fetch_loans_data(_self) -> pd.DataFrame:
        """Fetches the entire cached Loans table."""
        raise NotImplementedError()

    def filter_loans_data(_self, names: tuple[str] = ()) -> pd.DataFrame:
        """Gets loan items or all if no filters are provided."""
        df_raw = _self.fetch_loans_data()
        if names:
            return df_raw.query("name in @names")

        return df_raw

    @abstractmethod
    def fetch_expenses_data(_self) -> pd.DataFrame:
        """Gets the entire cached Expenses table."""
        raise NotImplementedError()

    def filter_expenses_data(_self, category: ExpenseCategory) -> pd.DataFrame:
        """Gets the expenses data by category."""
        df_raw = _self.fetch_expenses_data().query("category == @category")

        return df_raw.reset_index(drop=True).drop(columns="category")

    @abstractmethod
    def fetch_members_data(_self) -> pd.DataFrame:
        """Gets the entire cached Members table."""
        raise NotImplementedError()
