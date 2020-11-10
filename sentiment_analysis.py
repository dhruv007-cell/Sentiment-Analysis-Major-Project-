import numpy as np
import pandas as pd 
import pickle
import streamlit as st
import base64
from PIL import Image
model=pickle.load(open('sentiment_analysis_model.p','rb'))

st.set_page_config(page_title="Sentiment Analysis Web App",page_icon="",layout="centered",initial_sidebar_state="expanded",)
st.title('Sentiment Analysis Model')
st.subheader('by Amlan Mohanty ')

image='/content/drive/My Drive/sentiment.png'
st.image(image, caption='',use_column_width=False)


main_bg = "/content/drive/My Drive/wallpap.png"
main_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<style>
body {
    color: #ff0000;
    background-color: #001f;
    etc. 
}
</style>
    """, unsafe_allow_html=True)



st.subheader('Enter Text')
message = st.text_area("","Type Here ...")
if st.button('PREDICT'):
  disp=""
  a=model.predict([message])
  if(a == 'pos'):
        disp = "Positive Review!"
  else:
        disp = "Negative Review!"
  st.header(f"**{disp}**")
  

st.sidebar.subheader("About App")

st.sidebar.info("This web app is made as part of Sentiment Analysis Major Project")
st.sidebar.info("Scroll down and type your text in the writing area")
st.sidebar.info("Click on the 'Predict' button to check whether the entered text is 'Positive' or 'Negative' ")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=10,step=1)

if feedback:
  st.header("Thank you for rating the app!")
