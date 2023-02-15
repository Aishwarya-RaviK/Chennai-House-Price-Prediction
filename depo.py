#Importing neccessary libraries
import pandas as pd
import numpy as np
import streamlit as st
import pickle 
from sklearn.ensemble import GradientBoostingRegressor
import math
#Loading the model
pickle_file=open("chennaihouseprice_prediction.pkl","rb")
regressor=pickle.load(pickle_file)

#Function for the prediction
def prediction(AREA,INT_SQFT,N_BEDROOM,N_BATHROOM,PARK_FACIL,BUILDTYPE,STREET):
    if AREA=='Karapakkam':
        AREA=0
    elif AREA=='Adayar':
        AREA=1
    elif AREA=='Chrompet':
        AREA=2
    elif AREA=='Velachery':
        AREA=3
    elif AREA=='KK Nagar':
        AREA=4
    elif AREA=='Anna Nagar':
        AREA=5
    elif AREA=='T Nagar':
        AREA=6
    if STREET=='Paved':
        STREET=1
    elif STREET=='Gravel':
        STREET=2
    elif STREET=='No Access':
        STREET=0
    if BUILDTYPE=='House':
        BUILDTYPE=0
    elif BUILDTYPE=='Commercial':
        BUILDTYPE=2
    elif BUILDTYPE=='Others':
        BUILDTYPE=1
    if PARK_FACIL=='No':
        PARK_FACIL=0
    elif PARK_FACIL=='Yes':
        PARK_FACIL=1
    prediction=regressor.predict([[AREA,INT_SQFT,N_BEDROOM,N_BATHROOM,PARK_FACIL,BUILDTYPE,STREET]])
    return prediction 

def main():
#Image and title 

    page_bg_img ='''
    <style>
    body {
    background-image: url("light.avif");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.title('CHENNAI HOUSE PRICE PREDICTION')
    from PIL import Image 
    image=Image.open('background.jpg')
    st.image(image,caption='Check the price')
    st.header('Tell us about the property you want')

#The data to be provided
    AREA=st.selectbox('Area:',['Anna Nagar','Chrompet','Karapakkam','KK Nagar','Adayar','Velachery','T Nagar'])
    INT_SQFT=st.number_input('INT_SQFT',min_value=500)
    N_BEDROOM=st.number_input('N_BEDROOM',min_value=1,max_value=4)
    N_BATHROOM=st.number_input('N_BATHROOM',min_value=1,max_value=4)
    PARK_FACIL=st.selectbox('PARK_FACIL:',['Yes','No'])
    BUILDTYPE=st.selectbox('BUILDTYPE:',['House','Others','Commercial'])
    STREET=st.selectbox('STREET:',['Paved','No Access'])


#Button to predict
    if st.button("Check"):
        result=prediction(AREA,INT_SQFT,N_BEDROOM,N_BATHROOM,PARK_FACIL,BUILDTYPE,STREET)
        a=round(result[0])
        st.write('The cost of the property is Rs.')
        st.success(a)
if __name__=='__main__':
    main()







