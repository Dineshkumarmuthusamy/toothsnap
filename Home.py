import streamlit as st

create_page = st.Page("HomeContent.py", title="Home")
delete_page = st.Page("toothsnapapp.py", title="Prediction")

pg = st.navigation([create_page, delete_page])
st.set_page_config(page_title="Toothsnap",layout="wide", page_icon=":material/edit:")
pg.run()