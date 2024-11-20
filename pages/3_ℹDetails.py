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
    st.subheader('👋Information: ')
with st.container():
    st.write('-----')
    left_column,right_column=st.columns(2)
    with left_column:
        st.write('##')
        st.write("[Dataset used for Machine Learning Model Building🔍](https://www.kaggle.com/datasets/rabieelkharoua/air-quality-and-health-impact-dataset)")
    with right_column:
        st_lottie(lottie_coding,height=350,key='coding')