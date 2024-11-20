import streamlit as st
from streamlit_lottie import st_lottie
import requests
st.set_page_config(page_title='Air Quality Health Impact  Prediction',page_icon='😷',layout='wide')

def lottie_url(url):
    r= requests.get(url)
    if r.status_code!=200:
        return  None
    return r.json()

lottie_coding=lottie_url('https://lottie.host/5ed2a6df-1c8c-4607-bf93-2f16ba55b140/V8MWWOeIlx.json')

with st.container():
    st.subheader('👋Welcome to ')
    st.header('Air Quality Health Impact Prediction Site')
with st.container():
    st.write('-----')
    left_column,right_column=st.columns(2)
    with left_column:
        st.header('What is the need?')
        st.write('##')
        st.write('An air quality health impact prediction website is essential'
                 ' for helping people understand the potential health risks '
                 'associated with current air pollution levels. By providing real-time data'
                 ' on pollutants like AQI, PM10, PM2.5, NO2, and O3, the website can predict the severity of health impacts and offer actionable advice. This can help vulnerable groups, such as children, the elderly, and individuals with respiratory issues, take precautions to avoid harmful exposure. Additionally, such a platform can raise awareness about the importance of air quality and encourage communities to take steps to reduce pollution.')
        st.write("[Learn more about Air Quality around world 🔍](https://www.iqair.com/in-en/world-air-quality-ranking)")
    with right_column:
        st_lottie(lottie_coding,height=350,key='coding')