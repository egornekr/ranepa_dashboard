import streamlit as st
import random


st.set_page_config(
    page_title="RANEPA AI",
    page_icon="🦈")

st.header('Искусственный интеллект подберет тебе направление :sunglasses:')
st.write("![это ДАТА](https://media.giphy.com/media/rIq6ASPIqo2k0/giphy.gif)")

col1, col2 = st.columns(2)


with col1:
    science = st.slider('Я люблю науку', 0, 10, 5)
    creative = st.slider('Я креативщик', 0, 10, 5)

with col2:
    finance = st.slider('Я финансит', 0, 10, 5)
    social = st.slider('Я социальный', 0, 10, 5)

color = st.color_picker('Мой любимый цвет', '#00f900')

df = ['Бизнес-информатика','Гостиничное дело','Государственное и муниципальное управление','Журналистика','Лингвистика'
      'Международные отношения','Менеджмент','Политология','Правовое обеспечение национальной безопасности',
      'Психология', 'Реклама и связи с общественностью', 'Социальная работа','Социология','Таможенное дело',
      'Туризм','Экономика','Экономическая безопасность','Юриспруденция']


button = st.button('Дай мне ответ')

answer = random.sample(df,3)
if button:
    st.write(answer)
    st.text_input('Отправь мне информаци об этих направлениях')
    st.button('Отправляй уже') 