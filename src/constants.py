from enum import StrEnum, auto

DATABASE_ID = "analytics_db"


class TableName(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return f"{DATABASE_ID}.{name.lower()}"

    Contributions = auto()
    Loans = auto()
    Bank = auto()

    Expenses = auto()

    Members = auto()


# Expenses Table
class ExpenseCategory(StrEnum):
    INAUGURATION = "inauguration"
    INTEROGANIZATION_AFFAIRS = "interorganization affairs"
    MAINTENANCE = "maintenance"
    MEETINGS = "meetings"


# Bank Table
class BankCategory(StrEnum):
    INTEREST = "interest"
    TIME_DEPOSIT = "time deposit"


# Contribution Table
class DonorType(StrEnum):
    MEMBER = "member"
    ORGANIZATION = "organization"


class DonationCategory(StrEnum):
    DONATION = "donation"
    RAFFLE = "raffle"
    HOSPITALITY = "hospitality"


class DonationEvent(StrEnum):
    MID_AUTUMN_FESTIVAL = "中秋节"
