import streamlit as st

st.title("Streamlit Demo App 🚀")
st.markdown("Willkommen auf meine **Webseite**. Hier gibt es noch nicht viel zu sehen.")

username = st.text_input("Benutzername")
age = st.slider("Alter")

if st.button("Let Balloons fly"):
    st.balloons()


st.write(username.upper() + " " + str(age))