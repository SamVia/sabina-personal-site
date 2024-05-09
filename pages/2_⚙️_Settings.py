import streamlit as st

if "device" not in st.session_state:
    st.session_state.device = "desktop"


options = ["desktop", "mobile"]


st.session_state.device = st.radio("select orientation",options=options, key="option", index=options.index(st.session_state.device))
st.button("submit changes")