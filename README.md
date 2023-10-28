# Will my Flight be Delayed?
The goal of this project is to predict if a said flight will be delayed.

# Approach
I decided to use **PySpark** for this project. PySpark is the Python API written in python to support Apache Spark. Apache Spark is a distributed framework that can handle Big Data analysis. PySpark is a great language for performing exploratory data analysis at scale, building machine learning pipelines, and creating ETLs for a data platform. PySpark is a Python API for Spark released by the Apache Spark community to support Python with Spark.

# Dataset
[This](https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022/) is the dataset used for this project. The dataset contains information about various airlines. The dataset contains 61 columns and more than 10 Million Rows rows. The datasets were combined using Python. The dataset was cleaned and preprocessed using PySpark.

# Deployment
This is done using Docker and Streamlit, Visit the website:
https://delaydecoded.azurewebsites.net

OR

Run the following command:
<br>

Pull the docker image:
```
docker pull dockeramaan/pysparkproj
```
Run the docker image:
```
docker run -p 8501:8501 dockeramaan/pysparkproj
```
