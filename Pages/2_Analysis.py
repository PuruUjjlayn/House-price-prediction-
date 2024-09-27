import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

# title of page
st.set_page_config(page_title="Plotting Demo")

st.title('Analytics')

# new df
new_df = pd.read_csv('Pages\data_viz1.csv')

# group by data
group_df = new_df.groupby('sector')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()



# 1. Sector Price per Sqft Geomap
st.header('Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)
st.plotly_chart(fig,use_container_width=True)




# 2. Features Wordcloud
# feature pkl file
feature_data = pickle.load(open('Pages\sector_feature_dict.pkl','rb'))
sectors = list(feature_data.keys())
st.header('Features Wordcloud')
selected_sector = st.selectbox('Select Sector', sectors)
if selected_sector:
    feature_text = feature_data[selected_sector]
    wordcloud = WordCloud(width=800, height=800,
                          background_color='black',
                          stopwords=set(['s']),
                          min_font_size=10).generate(feature_text)
fig, ax = plt.subplots(figsize=(8, 8)) 
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)



#3. Area vs Price
st.header('Area Vs Price')
property_type = st.selectbox('Select Property Type', ['flat','house'])
if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")
    st.plotly_chart(fig1, use_container_width=True)


# BHK Pie Char
st.header('BHK Pie Chart')
sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')
selected_sector = st.selectbox('Select Sector', sector_options)
if selected_sector == 'overall':
    fig2 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)


# Side By Side BHK price comparison
st.header('Side by Side BHK price comparison')
fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig3, use_container_width=True)


# Side by Side Hist_Kde_plot for property type
st.header('Side by Side Hist kde plot for property type')
fig3 = plt.figure(figsize=(10, 4))
sns.histplot(new_df[new_df['property_type'] == 'house']['price'],label='house',kde=True)
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat',kde=True)
plt.legend()
st.pyplot(fig3)
