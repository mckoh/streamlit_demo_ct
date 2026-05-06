import streamlit as st

st.set_page_config(
    page_icon="🗺️",
    page_title="Quests",
    initial_sidebar_state="expanded",
    layout="centered"
)

if "quests" not in st.session_state:
    st.session_state["quests"] = []

st.title("Admin Screen")