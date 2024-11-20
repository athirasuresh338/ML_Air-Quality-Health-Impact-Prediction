import streamlit as st
import pickle
from PIL import Image

st.set_page_config(page_title='Air Quality Prediction',page_icon='😷',layout='wide')
def main():
    st.title('AIR QUALITY HEALTH IMPACT PREDICTION')
    img=Image.open('air quality.jpg')
    st.image(img,width=850)
    AQI=st.text_input('Enter AQI(air quality index)','')
    pm10=st.text_input('Conc. of particulate matter < 10 micrometres in diameter','')
    pm2_5=st.text_input('Conc. of particulate matter < 2.5 micrometres in diameter','')
    NO2=st.text_input('Conc. of Nitrogen dioxide','')
    SO2=st.text_input('Conc. of Sulphur dioxide','')
    O3=st.text_input('Conc. of Ozone','')
    temp=st.text_input('Temperature in degree Celsius','')
    humid=st.text_input('Humidity Percentage','')
    w_speed=st.text_input('Wind Speed in m/s','')
    hsptl_adm=st.text_input('Count of Hospital Admissions','')
    features=[AQI,pm10,pm2_5,NO2,SO2,O3,temp,humid,w_speed,hsptl_adm]
    model=pickle.load(open('AirQuality (1).sav','rb'))
    scaler=pickle.load(open('AQl_scaler.sav','rb'))
    pred=st.button('Predict')
    if pred:
        result=model.predict(scaler.transform([features]))
        if result==0:
            st.write('# Very High ')
        elif result==1:
            st.write('High')
        elif result==2:
            st.write('Moderate')
        elif result==3:
            st.write('Low')
        else:
            st.write('Very Low')
main()