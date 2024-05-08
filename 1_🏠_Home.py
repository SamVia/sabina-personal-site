
import streamlit as st
hide_st_style = """
    <style>
    footer {visibility: hidden;}
    header {visibility:hidden;}
    </stile>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
link = "https://github.com/SamVia/test_python/blob/main/combined_image.png?raw=true"
img_back=f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url({link});
background-size: 100% auto;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
overflow-y:auto;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(img_back,unsafe_allow_html=True)
for _ in range(524):
    st.write("\n")