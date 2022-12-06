import streamlit as st
import pandas as pd
from os import path

st.set_page_config(layout='wide')

data_dir = path.join(path.curdir, 'data')

st.title("My portfolio")
col1, col2 = st.columns(2)

with col1:
    st.image(path.join(data_dir, 'photo.jpg'))

with col2:
    st.title('Adam Templin')
    about_me = """
    Hi, I am Adam! I am a software developer, recently learning more about Python. I graduated System Engineering on Politechnika Wrocławska in 2015.
    I have worked in a big corporation with an international team, but it is time for me to move on to the next challenge.
    I enjoy problem solving involving programming, data manipulation as well as long walks with my dogs.
    """
    st.write(about_me)

content="""
Below you can find some of the apps I have built with Python. Feel free to contact me!
"""
st.subheader(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv(path.join(data_dir, 'data.csv'), sep=';')
print(df)

for start_point, col in enumerate([col3, col4]):
    with col:
        for index,row in df[start_point::2].iterrows():
            if row['completed'] == 'Yes':
                print(f'{index}, {row["title"]}')
                st.header(row['title'])
                st.write(f'{row["description"]}. To see this app, click [here]({row["url"]})')
                st.image(path.join(data_dir, row['image']))
