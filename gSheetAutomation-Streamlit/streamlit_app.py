import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd




   
# Selfmade depenendices
import utils as utl

# Data management
categories_file = r"C:\Users\matte\Desktop\Git\Pall0sProjects\gSheetAutomation-Streamlit\UsciteCTRL_19Mag2024.csv"
cat_database = utl.createCatDatabase( categories_file )

# Web App Management
st.title( "Expense Handler Portal")
st.markdown( "Questo è un messaggio di prova" )

# Connetting and getting existinga data as a pandas data frame
conn = st.connection( "gsheets" , type = GSheetsConnection )
existing_data = conn.read( worksheet = "Uscite"  , usecols = list( range( 6 ) ) , ttl = 5)
existing_data = existing_data.dropna( how = "all" )
expense_database = utl.createExpenseDatabase( existing_data )
#st.dataframe( existing_data )

# Page creation
expense_date = st.date_input( "Expense date")
expense_description = st.text_input( label = "Expense description" , key = "descr" )
expense_category = st.selectbox( "Categories" , cat_database.keys() , key = "cat" )
expense_subcategory = st.selectbox( "Subcategory" ,  options = cat_database[ expense_category ]  , key = "subcat")
expense_fixed = st.checkbox( label = "Fixed?" , key = "Fixed" )


add_button = st.button( label = "Add expense" )
match_button = st.button( label = "Match expense" ) 