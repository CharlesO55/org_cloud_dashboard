import streamlit as st
import pandas as pd


df_main = pd.DataFrame(columns=['Name', '金额'])


def load_income():
    items = [
        {
            'title' : "Donations",
            'filepath' : "data/1_2 donations.csv",
        },
        {
            'title' : "Organization Donations",
            'filepath' : "data/1_3 org donations.csv",
        },
        {
            'title' : "Event Donations",
            'filepath' : "data/1_4 event donations.csv",
        },
        {
            'title' : "Savings",
            'filepath' : "data/1_5 savings.csv",
        },
        {
            'title' : "Loans",
            'filepath' : "data/1_6 loans.csv",
        },
    ]


    income = {}
    for item in items:
        df = pd.read_csv(item.get('filepath')).select_dtypes(include='number')
        
        exclude_nums = ['年']
        
        df = df.drop(columns=exclude_nums, errors='ignore')

        income[item.get('title')] = df.sum().sum()


    return pd.DataFrame(pd.Series(income), columns=['Subtotal']).sort_values('Subtotal', ascending=False)


@st.cache_data
def load_expenses():
    items = [
        {
            'title' : "Ceremonies",
            'filepath' : "data/2_1 ceremonies.csv",
        },
        {
            'title' : "Monthly Meetings",
            'filepath' : "data/2_3 monthly meetings.csv",
        },
        {
            'title' : "Organizations",
            'filepath' : "data/2_4 organizations.csv",
        },
        {
            'title' : "Maintenance",
            'filepath' : "data/2_5 maintenance expenses.csv",
        },
    ]
    
    
    expenses = {}

    for item in items:
        expenses[item.get('title')] = pd.read_csv(item.get('filepath'))['金额'].sum() * -1

    return pd.DataFrame(pd.Series(expenses), columns=['Subtotal']).sort_values('Subtotal')
    

@st.cache_data
def load_old_balance():
    df = pd.read_csv('data/1_1 balance.csv', index_col=0)
    latest_year = df.index.max()

    return df.loc[latest_year]['金额']


df_income = load_income()
df_expenses = load_expenses()

latest_balance = load_old_balance()


with st.container(border=1):
    st.subheader("Summary")

    total_income = df_income.sum()
    total_expenses = df_expenses.sum()

    cols =  st.columns(3)

    with cols[0]:
        st.metric("Previous Surplus", latest_balance, format="%,.2f")

    with cols[1]:
        st.metric("Total Income", total_income, format="%,.2f")
    
    with cols[2]:
        st.metric("Total Expenses", total_expenses, format="%,.2f")

    st.divider()
    st.metric("Total Balance", latest_balance + total_income + total_expenses, format="%,.2f")


with st.container(border=1):
    st.subheader("Income")
    st.dataframe(df_income, column_config={"Subtotal" : st.column_config.NumberColumn(format="%,.2f")})
    st.bar_chart(df_income, horizontal=True)


with st.container(border=1):
    st.subheader("Expenses")
    st.dataframe(df_expenses, column_config={"Subtotal" : st.column_config.NumberColumn(format="%,.2f")})
    st.bar_chart(df_expenses.abs(), horizontal=True, color="#FF0000")