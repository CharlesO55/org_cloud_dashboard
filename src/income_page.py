import streamlit as st

from elements.generators.board_donations import board_dontations
from elements.generators.board_org_donations import board_org_dontations
from elements.generators.board_event_donations import board_event_donations
from elements.generators.board_savings import board_savings
from elements.generators.board_loans import board_loans


[tab_donations , 
 tab_org_donations , 
 tab_event_dontations , 
 tab_savings,
 tab_loans] = st.tabs([
    "Dontations", 
    "Org Dontations", 
    "Event Dontations", 
    "Savings",
    "Loans"
])


with tab_donations:
    board_dontations()

with tab_org_donations:
    board_org_dontations()

with tab_event_dontations:
    board_event_donations()

with tab_savings:
    board_savings()

with tab_loans:
    board_loans()