# Will my Flight be Delayed?
The goal of this project is to predict the arrival delay of a flight.

# Approach
I decided to use **PySpark** for this project. PySpark is the Python API written in python to support Apache Spark. Apache Spark is a distributed framework that can handle Big Data analysis. PySpark is a great language for performing exploratory data analysis at scale, building machine learning pipelines, and creating ETLs for a data platform. PySpark is a Python API for Spark released by the Apache Spark community to support Python with Spark.

# Dataset
[This](https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022/) is the dataset used for this project. The dataset contains information about various airlines. The dataset contains 61 columns and more than 10 Million Rows rows. The datasets were combined using Python. The dataset was cleaned and preprocessed using PySpark.

# Deployment
This is done using Docker and Streamlit, run the following command:
<br>
Git clone the repository:
```
git clone https://github.com/Amaaan09/pyspark-airport.git
```
Build the docker image:
```
docker build -t flight-delay .
```
Run the docker image:
```
docker run -p 8501:8501 flight-delay
```
