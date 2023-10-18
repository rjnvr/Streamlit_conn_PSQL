import streamlit as st
import psycopg2
import pandas as pd

st.title("PSQL Connection Test")
st.write("TEST WORKING")
# Initialize connection.
conn = st.experimental_connection("postgresql", type="sql")
conn
query = "SELECT * FROM inspection_dim WHERE inspection_result_cd = 'passed' limit 20;"
st.write(query)
df = conn.query(query, ttl="10m")
st.write(df)