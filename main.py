import streamlit as st
from os import path

data_dir = path.join(path.curdir, 'data')

col1, col2 = st.columns(2)

with col1:
    st.image(path.join(data_dir, 'photo.jpg'))

with col2:
    st.title('Adam Templin')
    content = """
    Hi, I am Adam! I am a software developer, recently learning more about Python. I graduated System Engineering on Politechnika Wrocławska in 2015.
    I have worked in a big corporation with an international team, but it is time for me to move on to the next challenge.
    I enjoy problem solving involving programming, data manipulation as well as long walks with my dogs.
    """
    st.write(content)
    