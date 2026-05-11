import streamlit as st
from datetime import date as dt

st.set_page_config(
    page_icon="🗺️",
    page_title="Quests",
    initial_sidebar_state="expanded",
    layout="centered"
)

if "quests" not in st.session_state:
    st.session_state["quests"] = []

if "my_quests" not in st.session_state:
    st.session_state["my_quests"] = []

st.title("Quests Screen")

st.markdown("Hier kannst du Quests erstellen, ansehen, verändern und annehmen.")
tab1, tab2, tab3 = st.tabs([
    "Neue Quest",
    "Alle Quests",
    "My Quests"
])

with tab2:
    if st.button("Reload", key="quests_reload"):
        st.rerun()
    st.header("Alle Quests")
    st.markdown("Unterhalb findest du eine Liste mit Challenges, die du absolvieren kannst. Wähle eine Challenge aus, indem du auf den Button klickst.")
    st.markdown("---")

    for i, quest in enumerate(st.session_state["quests"]):
        if quest["date"] > dt.today():
            st.subheader(quest["subject"])
            st.markdown(quest["description"])
            if st.button("Join this Quest", key=str(i)):
                st.session_state["my_quests"].append(i)
            st.markdown("---")

with tab1:
    st.header("Neue Quests")
    subject = st.text_input("Subject")
    description = st.text_input("Description")
    level = st.slider("Level", min_value=1, max_value=5, step=1)
    date = st.date_input("End Datum")

    if st.button("Submit"):
        quest = {
            "subject": subject,
            "description": description,
            "level": level,
            "date": date
        }
        st.session_state["quests"].append(quest)
        st.write(f"Neue Challenge hinzugefügt: {subject}")

with tab3:
    if st.button("Reload", key="my_quests_reload"):
        st.rerun()
    st.header("Meine Quests")
    st.markdown("An folgenden Quests nimmst du aktuell teil.")
    st.markdown("---")
    for i in st.session_state["my_quests"]:
        quest = st.session_state["quests"][i]
        st.subheader(quest["subject"])
        st.markdown(quest["description"])
        if st.button("Join this Quest", key="my"+str(i)):
            st.session_state["my_quests"].remove(i)
        st.markdown("---")