# Will my Flight be Delayed?
The goal of this project is to predict the arrival delay of a flight.

# Dataset
[This](https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022/) is the dataset used for this project. The dataset contains information about various airlines. The dataset contains 61 columns and more than 10 Million Rows rows. The datasets were combined using Python. The dataset was cleaned and preprocessed using PySpark. The main ipynb is currently private and will be made public once it is documented properly.


# Deployment
This is done using Docker and Streamlit, just run the following command:
Build the docker image:
```
docker build -t flight-delay .
```
Run the docker image:
```
docker run -p 8501:8501 flight-delay
```
