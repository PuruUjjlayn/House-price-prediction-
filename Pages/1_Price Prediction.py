import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title='Plotting Demo')

with open(r'C:\Users\puruc\Downloads\render-projects\House-Price-Prediction\Pages\df.pkl','rb') as file :
    df = pickle.load(file)

with open(r'C:\Users\puruc\Downloads\render-projects\House-Price-Prediction\Pages\best_pipeline.pkl','rb') as file :
    pipeline = pickle.load(file)

st.header('Enter your input')

# Collect user input from the interface
property_type = st.selectbox('Property_type',['flat','house'])
sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))
bedrooms = float(st.selectbox('Bedrooms',sorted(df['bedRoom'].unique().tolist())))
bathroom = float(st.selectbox('Bathrooms',sorted(df['bathroom'].unique().tolist())))
balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))
agepossession = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))
area = float(st.number_input('Area'))
servantroom = st.selectbox('Servant room',['Yes','No'])
furnishing_type = st.selectbox('Furnishing_type',sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    data = [[property_type, sector, bedrooms, bathroom, balcony, agepossession, area, servantroom, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'super_built_up_area', 'servant room',
               'furnishing_type', 'luxury_category', 'floor_category']
    one_df = pd.DataFrame(data, columns=columns)
    #st.dataframe(one_df)

    # Prediction
    base_price = float(np.expm1(pipeline.predict(one_df))[0])
    low = base_price - 0.22
    high = base_price + 0.22

    # Display the result
    st.text(f"The price of the flat is between {round(low, 2)} cr and {round(high, 2)} cr")
