import streamlit as st

from src.elements.generators.board_contributions import board_contributions
from src.elements.generators.board_loans import board_loans
from src.elements.generators.board_bank import board_bank

[tab_contributions, tab_savings, tab_loans] = st.tabs(
    ["Contributions", "Bank", "Loans"]
)


with tab_contributions:
    board_contributions()

with tab_savings:
    board_bank()

with tab_loans:
    board_loans()
