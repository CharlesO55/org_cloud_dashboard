import streamlit as st
from login_page import is_authenticated

login_page = st.Page("login_page.py", title="Log In", icon="🔒")
summary_page = st.Page("summary_page.py", title="Summary", icon="📊")
income_page = st.Page("income_page.py", title="Income", icon="💲")
expenses_page = st.Page("expenses_page.py", title="Expenses", icon="💳")


if is_authenticated():
    pages_dict = {
        "Finances" : [summary_page, income_page, expenses_page],
    }

    pg = st.navigation(pages_dict)
else:
    pg = st.navigation([login_page])

pg.run()