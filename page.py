import streamlit as st
import pandas as pd
from pyspark.ml import PipelineModel


st.title("DelayDecoded")

df = pd.read_csv("airport-data.csv")

st.sidebar.title("Input Features")

st.sidebar.markdown("Select the features that you want to input.")

airline = st.sidebar.selectbox("Airline", df["Airline"].unique())
origin = st.sidebar.selectbox("Origin", df["Origin"].unique())
dest = st.sidebar.selectbox("Destination", df["Dest"].unique())
distance = st.sidebar.number_input("Distance", value=df['Distance'].mean())
year = st.sidebar.number_input("Year", value=int(df['Year'].median()))
quarter = st.sidebar.number_input("Quarter", value=int(df['Quarter'].median()))
month = st.sidebar.number_input("Month", value=int(df['Month'].median()))
day_of_month = st.sidebar.number_input("Day of Month", value=int(df['DayofMonth'].median()))
day_of_week = st.sidebar.number_input("Day of Week", value=int(df['DayOfWeek'].median()))
marketing_airline_network = st.sidebar.selectbox("Marketing Airline Network", df["Marketing_Airline_Network"].unique())
operated_or_branded_code_share_partners = st.sidebar.selectbox("Operated or Branded Code Share Partners", df["Operated_or_Branded_Code_Share_Partners"].unique())
iata_code_marketing_airline = st.sidebar.selectbox("IATA Code Marketing Airline", df["IATA_Code_Marketing_Airline"].unique())
operating_airline = st.sidebar.selectbox("Operating Airline", df["Operating_Airline"].unique())
iata_code_operating_airline = st.sidebar.selectbox("IATA Code Operating Airline", df["IATA_Code_Operating_Airline"].unique())
crs_arr_time = st.sidebar.number_input("CRS Arrival Time", value=df['CRSArrTime'].median())
crs_dep_time = st.sidebar.number_input("CRS Departure Time", value=df['CRSDepTime'].median())
crs_elapsed_time = st.sidebar.number_input("CRS Elapsed Time", value=df['CRSElapsedTime'].median())


if st.button("Predict"):
    st.write("Predicted Delay: 10")
    model = PipelineModel.load('airport-index/')
    print('model loaded')

