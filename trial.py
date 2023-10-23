from pyspark.ml import PipelineModel

model = PipelineModel.load('files/airport-shiz/')
print("Model loaded")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("bigData").getOrCreate()

df = spark.read.csv("airport-data.csv", header=True, inferSchema=True)
print("Data loaded")
