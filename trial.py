from pyspark.ml import PipelineModel
import streamlit as st

model = PipelineModel.load('files/airport-shiz/')
print("Model loaded")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("bigData").getOrCreate()

df = spark.read.csv("airport-data.csv", header=True, inferSchema=True)
print("Data loaded")

st.title("Airport Prediction shiz")

st.write("This is a simple web app to predict the airport based on the input data")