import streamlit as st
import joblib
import numpy as np

st.title('Car-Price Predictor')


Cars_name=joblib.load('car_price_prediction_new.pkl')

df=joblib.load('car_price_prediction_df.pkl')

model=joblib.load('car_price_prediction.pkl')


Car=st.selectbox('Select the car you want to sell',Cars_name['Car_Name'].unique())

Price = st.selectbox('Present-Price', df['Present_Price'].unique())

Km=st.selectbox('KM-Driven',df['Kms_Driven'].unique())

FuelType=st.selectbox('Fuel-Type',['Petrol','Diesel','CNG'])
Seller=st.selectbox('Seller',['Dealer','Individual'])

Trans=st.selectbox('Transmission',['Manual','Automatic'])

Owner=st.selectbox('Owner',['Yes','No'])

Age=st.selectbox('Age of the car',df['Age'].unique())

if st.button('Predict-Price'):
    
    if FuelType=='Petrol':
        FuelType=0
    elif FuelType=='Diesel':
        FuelType=1
    else:
        FuelType=2
        
    if Seller=='Dealer':
        Seller=0
    else:
        Seller=1
        
    if Trans=='Manual':
        Trans=0
    else:
        Trans=1
        
    if Owner=='Yes':
        Owner=1
    else:
        Owner=0
        
    
    q=[]
    q=np.array([Price,Km,FuelType,Seller,Trans,Owner,Age])
    q = q.reshape(1, -1)  # Convert to 2D array with one row
    st.title(model.predict(q))





