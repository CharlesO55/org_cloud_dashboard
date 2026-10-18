from enum import StrEnum, auto

DATABASE_ID = "analytics_db"


class TableName(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return f"{DATABASE_ID}.{name.lower()}"

    Contributions = auto()
    Loans = auto()
    Savings = auto()

    Expenses = auto()

    Members = auto()


class ExpenseCategory(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return f"{name.lower().replace('_', ' ')}"

    Inauguration = auto()
    Interorganization_affairs = auto()
    Maintenance = auto()
    Meetings = auto()
