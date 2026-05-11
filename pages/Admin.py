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

if st.button("Reload", key="my_quests_reload"):
    st.rerun()
st.markdown("---")
for i, quest in enumerate(st.session_state["quests"]):
    st.subheader(quest["subject"])
    st.markdown(quest["description"])
    if st.button("Delete Quest forever", key="all"+str(i)):
        st.session_state["quests"].remove(quest)
    st.markdown("---")