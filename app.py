import streamlit as st
from home_page import display_home
from prediction_page import display_prediction
from analysis_page import display_analysis
from recommendation_page import display_recommendation

st.set_page_config(page_title='Real Estate Data Science Project', layout='wide')

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Price Prediction", "Analytics", "Recommendation"])

if page == "Home":
    display_home()
elif page == "Price Prediction":
    display_prediction()
elif page == "Analytics":
    display_analysis()
elif page == "Recommendation":
    display_recommendation()