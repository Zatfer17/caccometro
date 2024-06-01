import streamlit as st
import shutil
import os
import ast

from datetime import date

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    with open("./chats/chat.zip", "wb") as f:
        f.write(uploaded_file.getbuffer())
    shutil.unpack_archive('./chats/chat.zip', './chats', 'zip')
    files = os.listdir('./chats/')
    for file in files:
        if '.txt' in file:
            file_name = file
            break
    with open(f"./chats/{file_name}", "r", encoding="utf8") as f:
        text = f.read()
    text = text.split('\n')

    today = date.today().strftime("%d/%m/%y")
    daily_scores = {}

    today_messages = []
    for line in text:
        if (today in line):
            elements = line.split('-')
            message = elements[1]
            if '💩' in message:
                elements = message.split(':')
                person = elements[0]
                message = elements[1]
            
                if person not in daily_scores:
                    daily_scores[person] = 0
                daily_scores[person] += 1
            today_messages.append(elements)

    st.write(daily_scores)

    files = os.listdir('./chats/')
    for f in files:
        os.remove(f"./chats/{f}")
