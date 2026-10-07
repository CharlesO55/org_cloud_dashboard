import streamlit as st

from datetime import datetime , timedelta


def is_authenticated():
    auth_expiry = st.session_state.get("auth_expiry")
    if auth_expiry and auth_expiry > datetime.now():
        refresh_auth()
        return True

    return False

def refresh_auth():
    st.session_state['auth_expiry'] = datetime.now() + timedelta(hours=1)


def login_screen():
    st.header("Authentication Required")
    
    with st.form("login_form"):
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Log In")
        
        if submit:
            if password == st.secrets["auth_password"]:
                refresh_auth()            
                st.rerun() 
            else:
                st.error("Invalid Password")



if __name__ == "__main__":
    login_screen()