import streamlit as st

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
    if st.button("Reload"):
        st.rerun()
    st.header("Alle Quests")

    for i, quest in enumerate(st.session_state["quests"]):
        st.write(quest["subject"])
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
    st.header("Meine Quests")
    st.write(list(set(st.session_state["my_quests"])))