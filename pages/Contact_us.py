import streamlit as st
import pandas
import os
from send_email import send_email

# Get the current working directory
current_dir = os.path.dirname(__file__)

# Construct the path to topics.csv
csv_path = os.path.join(current_dir, '..', 'topics.csv')
print(csv_path)
df = pandas.read_csv(csv_path)
topics = []

for index, row in df[:len(df)].iterrows():
    print(row["topic"] + " LFUDls")
    topics.append(row["topic"])


st.header("Contact me")

with st.form(key="my_form"):
    email = st.text_input("Your email")

    option = st.selectbox("What topic do you want to discus", options=topics)

    my_text = st.text_area("Your message")

    letter = f"""\
Subject: {option}
{my_text}
From {email}
"""
    button = st.form_submit_button()
    if button:
        send_email(letter)
        st.info("Your email was send succesfully")