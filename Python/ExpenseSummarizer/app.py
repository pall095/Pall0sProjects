import streamlit as st
from src.classes.DdManager import DbManager


ENTRY_TYPES = [ "Liquitidy" , "Investments" ]

LIQUID_SOURCES = [
    "Azzaglio" ,
    "Revolut" ,
    "Fideuram" ,
    "Paypal" ,
    "Satispay" ,
    "Contanti"
]

INVESTMENTS_SOURCES = [
    "Fideuram - BTP" ,
    "Revolut - Invest" ,
    "Revolut - Savings" ,
    "Allianz" ,
    "Affidati"
]

manager = DbManager( "entries_test.csv" ) 


date = st.date_input("Select Date")

entry_type = st.selectbox(
    label="Select Entry Type",
    options=ENTRY_TYPES
)

if entry_type == "Liquitidy":
    source = st.selectbox(
        label="Select Source",
        options=LIQUID_SOURCES
    )
else:
    source = st.selectbox(
        label="Select Source",
        options=INVESTMENTS_SOURCES
    )

with st.form("Add your financial entry"):
    amount = st.number_input(
        "Amount (€)",
        min_value=0.0,
        step=0.01,
        format="%.2f"
    )

    comment = st.text_input("Comments")

    submitted = st.form_submit_button("Submit entry")

if submitted :
    entry_dict = { 
            "type" : entry_type ,
            "source" : source ,
            "amount" : amount , 
            "date" : date ,
            "comment" : comment
    }
    manager.append_entry( entry_dict )
    manager.write( )



