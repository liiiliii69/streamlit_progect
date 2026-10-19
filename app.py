import streamlit as st
import pandas as pd
import numpy as np

st.title('STREAMLIT PROJECT')

st.write('first app')

age = st.slider('enter your age',min_value=10, max_value=90, step=5)
st.write(f'your age is {age}')

city = st.selectbox('Select Your City', 
    ('Tehran', 'Isfahan', 'Tabriz', 'Ahwaz', 'Shiraz'), index=3)
st.write(f'your city is {city}')

hobbies = st.multiselect('Select Your hobbies',
                         ('Movie', 'Sport', 'Music', 'Study', 'Driving'),
                           max_selections=2)
st.write(f'your hobbies is {hobbies}')

grade = st.number_input('enter your grade', min_value=10, max_value=100, step=2)

name = st.text_input('Enter your name', max_chars=10, placeholder='example: Ali')

description = st.text_area('Enter Your description', max_chars=100)

switch = st.toggle('ON/OFF')
if switch:
    st.balloons()

degree = st.radio('Select Your degree',
                  ('BE', 'MS', 'PHD', 'POSTDOC'))
st.write(f'your hobbies is {degree}')

show = st.checkbox('SHOW/HIDE snow')
if show:
    st.snow()

df = pd.DataFrame(np.random.randn(20,4),columns=['X', 'Y', 'Z', 'T'])
# st.bar_chart(df)
# st.line_chart(df)




st.metric('Tempreture', value='69', delta=-2.3)

col1, col2 = st.columns(2)
col1.title('First Column')
col1.slider('select age', 10,50)

col2.title('Second Column')
col2.number_input('enter salary')



st.sidebar.title('filter option')
option = st.sidebar.selectbox('Select Your Option',
                     ('Image', 'Audio','Data', 'LineChart', 'BarChart'))
if option == 'Image':
    st.image('image/1041.jpg')
elif option == 'Audio':
    st.audio('audio/Chavoshi.mp3')

elif option == 'Data':
    st.table(df)

elif option == 'LineChart':
    st.line_chart(df)

elif option == 'BarChart':
    st.bar_chart(df)