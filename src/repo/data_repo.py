from abc import ABC, abstractmethod

import pandas as pd

from src.constants import DonorType, DonationCategory, DonationEvent, BankCategory


class DataRepo(ABC):
    """Container for fetch data methods."""

    @abstractmethod
    def get_bank_data(_self, category: BankCategory | None) -> pd.DataFrame:
        """Gets bank account items or all if no filters are provided."""

    @abstractmethod
    def get_contributions_data(
        _self,
        donor_type: DonorType | None = None,
        category: DonationCategory | None = None,
        event: DonationEvent | tuple[DonationEvent] = (),
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
