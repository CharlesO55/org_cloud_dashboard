import streamlit as st
from elements.expenses.board_maintenance import board_maintenance
from elements.expenses.board_meetings import board_meetings
from elements.expenses.board_ceremonies import board_ceremonies
from elements.expenses.board_organizations import board_oganizations

[tab_maintenance,
 tab_organizations,
 tab_meetings,
 tab_ceremony
 ] = st.tabs([
    "Maintenance",
    "Ogranizations",
    "Meetings",
    "Ceremony",
])



with tab_maintenance:
    board_maintenance()

with tab_meetings:
    board_meetings()

with tab_ceremony:
    board_ceremonies()

with tab_organizations:
    board_oganizations()