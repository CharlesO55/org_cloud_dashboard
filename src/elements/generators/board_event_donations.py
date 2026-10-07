import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    df_raw = pd.read_csv("data/1_4 event donations.csv")
    festival_choices = df_raw['节日'].unique() 
    year_choices = df_raw['年'].unique() 


    return df_raw, festival_choices, year_choices


def board_event_donations():
    df_raw, festival_choices, year_choices = load_data()

    with st.container(border=1):
        st.info("Select an event and year")
        
        cols = st.columns(2)
        with cols[0]:
            selected_festivals = st.multiselect(
                label="节日",
                options=festival_choices,
                default=festival_choices,
            )    
        
        with cols[1]:
            selected_years = st.multiselect(
                label="年",
                options=year_choices,
                default=year_choices,
            )    


    df_splice = df_raw[
        df_raw["年"].isin(selected_years) &
        df_raw["节日"].isin(selected_festivals)
    ]
    
    df_summary = df_splice.groupby(["年", "节日"], as_index=False)["捐"].sum()



    with st.container(border=1):
        st.subheader("Metrics")
        st.metric('捐 Total', df_splice['捐'].sum(), format="%,d")


    with st.container(border=1):
        st.subheader("Records")
        col_config = {
            "捐" : st.column_config.NumberColumn(format="%,d"),
        }
        st.dataframe(df_splice, column_config=col_config)



    with st.container(border=1):
        st.subheader("Timeline")
        
        st.bar_chart(
            df_summary,
            x="年",
            y="捐",
            color="节日"
        )