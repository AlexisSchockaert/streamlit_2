import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np

st.title('Cars')

# streamlit run my_streamlit_app.py

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)

df_car

# df_car.columns

liste_pays = df_car['continent'].unique()

# Here we use "magic commands", c-a-d au lieu de st.write(df_weather):

viz_correlation = sns.heatmap(df_car.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)


liste_continent= df_car['continent'].unique()
    
continent_selection = st.sidebar.selectbox(label="Veuillez sélectionner un continent",
                                        options = liste_continent,
                                        index=1)

condition = continent_selection == df_car['continent']

df_filter = df_car.loc[condition,:]
df_filter