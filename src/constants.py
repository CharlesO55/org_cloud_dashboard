from enum import StrEnum, auto

DATABASE_ID = "analytics_db"


class TableNames(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return f"{DATABASE_ID}.{name.lower()}"

    contributions = auto()
    loans = auto()
    savings = auto()

    expenses = auto()

    members = auto()
