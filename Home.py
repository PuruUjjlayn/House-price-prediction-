import streamlit as st

st.set_page_config(
    page_title='Home - Data Science Project Of Real State'
)

st.write('# Welcome to My Data Science Project!')

st.markdown("""
## About This Project
I am passionate about data science and have developed this project to explore and predict house prices, visualize property data, and recommend apartments based on user preferences. This project involves three main sections:

1. **Price Prediction**: Predict property prices based on various factors such as sector, bedrooms, bathrooms, and more.
2. **Visualization**: Analyze and visualize data trends, price distributions, and sector-wise insights.
3. **Recommendation**: Suggest similar properties based on user-selected apartments and proximity preferences.

## Project Overview
This project was completed in six key steps:

1. **Data Gathering**: Collecting a comprehensive dataset on properties in Gurgaon.
2. **Data Cleaning**: Ensuring the data is free from inconsistencies, missing values, and errors.
3. **Feature Engineering**: Extracting and creating relevant features for better model performance.
4. **Exploratory Data Analysis (EDA)**: Visualizing the data to discover trends and patterns.
5. **Model Building**: Using advanced machine learning algorithms to predict house prices with precision.
6. **Recommendations**: Providing property recommendations based on similarity scores and location proximity.
            
## How This Project Can Help You
This project is designed to assist homebuyers, real estate agents, and property investors by providing:

- **Accurate Price Predictions**: Get an estimated price range for properties based on real data, helping you make informed decisions when buying or selling homes.
- **Insightful Data Visualization**: Visualize trends, such as price per square foot across different sectors, and identify the best areas for investment.
- **Tailored Property Recommendations**: Receive personalized property suggestions based on your preferences, including proximity to desired locations, property features, and similarity to other homes.

By leveraging advanced machine learning models and data analysis techniques, this project provides valuable insights and tools to navigate the real estate market more efficiently.

Feel free to explore each section from the sidebar to see the predictive models, interactive visualizations, and property recommendations in action.
""")

st.sidebar.success('Select a anyone feature from the sidebar.')
