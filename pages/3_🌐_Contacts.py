import streamlit as st
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
if "device" not in st.session_state:
    st.session_state.device = "desktop"


SENDGRID_API_KEY = st.secrets["mail"]

def button_logo(site, logo, circle):
    """generates markdown for a button to a site
    accepts site link, logo link better if png, and circle is true if the logo is circular else false
    """
    if circle: circle = "border-radius:50%;"
    else: circle = ""
    return f"""
<style>
    .myButton {{
        background-color: transparent;
        color: white;
        padding: 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 0px;
        cursor: pointer;
        border: none;
        border-radius: 50%;
        transition: transform .2s;
        outline: none;
        position:relative;
    }}

    .myButton:hover {{
        transform: scale(1.1);
    }}
</style>

<a href="{site}" class="myButton" target="_blank">
    <button class="myButton">
        <img src="{logo}" alt="Image description" style="width:100px;height:100px;{circle}">
    </button>
</a>
"""

def send_email(sender_email, receiver_email, subject, message):
    message = Mail(
        from_email=sender_email,
        to_emails=receiver_email,
        subject=subject,
        plain_text_content=message)

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print("Email sent successfully!")
        return True
    except Exception as e:
        print("Error:", e)
        return False


sender_email = st.secrets["sender"]

receiver_email = st.secrets["receiver"]
subject = st.text_input("Mittente",key="sender")
message = st.text_input("Inserisci messaggio", key = "message")
if st.button("Invia", key="send"):
    if send_email(sender_email, receiver_email, subject, message):
        print("Email sent successfully!")
        st.success("Email mandata correttamente!")
    else:
        print("Failed to send email.")
        st.error("Errore nell'inviare email.")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(button_logo("","https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png", True), unsafe_allow_html=True)
with col2:
    st.markdown(button_logo("","https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png", True), unsafe_allow_html=True)
with col3:
    st.markdown(button_logo("","https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png", True), unsafe_allow_html=True)
with col4:
    with open("Pascuttini Sabina - curriculum.pdf", "rb") as f:
        st.write("\n")
        st.download_button("Download il CV:",data=f, file_name="Pascuttini Sabina - curriculum.pdf")