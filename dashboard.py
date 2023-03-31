import streamlit as st
import random
import requests
from streamlit_lottie import st_lottie
import time



st.set_page_config(
    page_title="RANEPA AI",
    page_icon="🎓")

# ---- USE LOCAL CSS ----

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")


# ---- HEADER SECTION ----

st.title('Искусственный интеллект подберет тебе направление :sunglasses:')

# ---- ANIMATION ----

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_pJvtiSVyYH.json')

st_lottie(lottie,height=200)

# ---- MAIN CODE ----

col1, col2 = st.columns(2)

with col1:
    science = st.slider('🔬 Я люблю науку', 0, 10, 5)
    creative = st.slider('🔥 Я креативщик', 0, 10, 5)

with col2:
    finance = st.slider('🤑 Люблю денежку', 0, 10, 5)
    social = st.slider('👐 Я социальный', 0, 10, 5)

genre = st.radio(
    "Твой пол",
    ('👨', '👩','😹'),horizontal=True)


color = st.color_picker('Твой любимый цвет',  '#9c1458')

df = ['Бизнес-информатика','Гостиничное дело','Государственное и муниципальное управление','Журналистика','Лингвистика',
      'Международные отношения','Менеджмент','Политология','Правовое обеспечение национальной безопасности',
      'Психология', 'Реклама и связи с общественностью', 'Социальная работа','Социология','Таможенное дело',
      'Туризм','Экономика','Экономическая безопасность','Юриспруденция']


button = st.button('Дай мне ответ')

answer = random.sample(df,3)
if button:
    with st.spinner('Анализирую...'):
        time.sleep(1)
    st.write("Тебе подходят:")
    if genre == '😹':
        st.markdown("[Невские титаны](https://spb.ranepa.ru/students-zhizn/studencheskij-sportivnyj-klub-nevskie-titany/)")
    else:
        st.markdown(f"[{answer[0]}](https://priem.spb.ranepa.ru/bakalavriat-i-specialitet/)")
        st.markdown(f"[{answer[1]}](https://priem.spb.ranepa.ru/bakalavriat-i-specialitet/)")
        st.markdown(f"[{answer[2]}](https://priem.spb.ranepa.ru/bakalavriat-i-specialitet/)")



st.write("---")

st.write("Хочешь к нам поступить?")

# ---- CONTACT FORM ----

contact_form = '''
<form action="https://formsubmit.co/egorn@bk.ru" method="POST">
    <input type="hidden" name = "_captcha" value = "false">
     <input type="text" name="name" placeholder = 'Имя' required>
     <input type="text" name="grade" placeholder = 'В каком классе учишься?' required>
     <input type="email" name="email" placeholder = 'Email' required>
     <button type="submit">Отправьте мне информацию</button>
</form>

'''
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()


# ---- end logo ----

st.markdown('''
    <a href="https://spb.ranepa.ru/">
        <img src="https://spb.ranepa.ru/wp-content/uploads/2020/11/logo_ranepaspb.png" width="250" class="center"/>
    </a>''',
    unsafe_allow_html=True
)