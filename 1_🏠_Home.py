
import streamlit as st

st.set_page_config(initial_sidebar_state="expanded")

hide_st_style = """
    <style>
    footer {visibility: hidden;}
    header {visibility:hidden;}
    </stile>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

if "device" not in st.session_state:
    st.session_state.device = "desktop"


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
# st.markdown("""<style>
#     [data-testid="stSidebarNavSeparator"] {
#         display: none;
#     }
# </style>
# """, unsafe_allow_html=True)
# with st.sidebar:
#     sidebar="""<style>
#     [data-testid="stSidebar"] {
#         background: LightBlue;
#         display: flex;
#         flex-direction: column;
#         justify-content: space-between;
#         position: relative;
#     }
#     [data-testid="stSidebar"] .footer {
#         text-align: center;
#         width: 100%;
#         position:relative;
#         top:40vh;
#     }
# </style>
# <div data-testid="stSidebar">
#     <div></div>
#     <div class="footer">
#         Your text here
#     </div>
# </div>
#     """


#     st.markdown(sidebar,unsafe_allow_html=True)
if st.session_state.device == "desktop":
    for _ in range(523):
        st.write("\n")
elif st.session_state.device == "mobile":
    for _ in range(120):
        st.write("\n")