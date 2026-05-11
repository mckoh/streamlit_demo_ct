import streamlit as st

st.set_page_config(
    page_icon="🗺️",
    page_title="Quests",
    initial_sidebar_state="expanded",
    layout="centered"
)

if "quests" not in st.session_state:
    st.session_state["quests"] = []

st.title("Streamlit Demo App 🚀")
st.markdown("""Die **GroupQuest-App** soll Menschen motivieren, gemeinsam an kleinen Herausforderungen dranzubleiben und Erfolge sichtbar zu machen. Nutzer:innen erstellen Challenges mit klaren Regeln, Dauer und Anforderungen und teilen sie öffentlich oder in Gruppen.

Teilnehmende dokumentieren Fortschritt über Check-ins, Fotos oder Texte, die automatisch oder durch die Gruppe bestätigt werden können. Ein Punkte-, Level- und Badge-System belohnt Konsistenz und steigert die langfristige Motivation. Leaderboards und ein Social Feed schaffen sozialen Anreiz, Austausch und freundlichen Wettbewerb.""")

st.markdown("Hallo Welt.")