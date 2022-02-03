import streamlit as st
import numpy as np
import string
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = joblib.load(open('model.joblib','rb'))


def main():
  st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Slip to Slip connection Time</h1>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: center; color: Black;'>Data Scientist Challenge Intelie</h4>", unsafe_allow_html=True)
  st.sidebar.header("What is this Project about?")
  st.sidebar.text("It is a Web app that would help the user in determining whether the Slips is on or off during a drilling operation.")
  

  bdep = st.slider("bit depth in m",0,10000)
  hl = st.slider("hook load in klbf",0,1000)
  bht = st.slider("block position in m",0,1000)
  dept = st.slider("hole depth in m",0,10000)
  wob = st.slider("weight on bit in klbf",0,1000)

  inputs = [[bdep,hl,bht,dept,wob]]

  pipe = Pipeline([('scaler', Normalizer()), ('model', model)])

  

  if st.button('Predict'):
    result = pipe.predict(inputs)
    updated_res = result
    if updated_res == 0:
      st.success('The Slips is Off')
    elif updated_res == 1:
      st.success('The Slips is On')


if __name__ =='__main__':
  main()