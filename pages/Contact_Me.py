import streamlit as st
from send_email import send_email

st.header('Contact me')

with st.form(key='email_form'):
    user_email = st.text_input('Your email adress:')
    raw_message = st.text_area('Your message:')

    message = f'Subject: New mail from {user_email}\n'
    message += raw_message + '\n'
    message += user_email

    submit_button = st.form_submit_button('Send an email')
    if submit_button:
        send_email(message)
        st.info("Your email was sent successfully")