import streamlit as st
import time
if "device" not in st.session_state:
    st.session_state.device = "desktop"
st.session_state.device

options = ["desktop", "mobile"]


st.session_state.device = st.radio("select orientation",options=options, key="option", index=options.index(st.session_state.device))
st.button("submit changes")