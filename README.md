# Medicinal Plant Identification System:

## Introduction about the Project:
In recent years, there has been a growing interest in the utilization of medicinal plants for their therapeutic properties. Recognizing the importance of accurate plant identification for herbal medicine and botanical research, we have developed a Medicinal Plant Identification System. This innovative project harnesses the power of technology to facilitate the identification and categorization of various medicinal plants.

## Objective :
The primary objective of our Medicinal Plant Identification System is to provide a reliable and efficient tool for botanists, herbalists, researchers, and enthusiasts to quickly identify medicinal plants based on their visual attributes. This system aims to bridge the gap between traditional knowledge of plant identification and modern technological advancements, making it easier for users to access information about the medicinal properties of plants.

## Website of project:
<img src="https://github.com/poriyaKuldeep/Medicinal-Plant-Identification-System/blob/main/Screenshot%20(29).png">


## Table Of Contents

-   [Data Collection](##1-data-collection)
-   [Data Cleaning & Preprocessing](#2-data-cleaning--preprocessing)
-   [Data Augmentation](#3-data-augmentation)
-   [Model Creation](#4-model-creation)
-   [Model Optimization](#5-model-optimization)
-   [Write Python Backend Server](#6-write-python-backend-server)
-   [Integrate Frontend with Backend](#7-integrate-frontend-with-backend)
  



 <h1> Approach for the project.</h1>

## 1. Data Collection :<br>
   * We used Indian Medicinal Plants Dataset from kaggle for Our Project:<br>
   * [https://www.kaggle.com/datasets/aryashah2k/indian-medicinal-leaves-dataset]

## 2. Data Cleaning & Preprocessing :<br>
   * Used tf data Input pipeline to load data Into batches and for utilization of Ram.
   * Also for data cleaning and preprocessing task like resize and rescale we used tf dataset, which make our task very easy in compact formate.

## 3. Data Augmentation :<br>
   * Deep Learning Model is data hungry..., sometimes we have not suffecient data to train our model In that case by using data Augmentation we can generate new data by performing some task on original data like...<br>
         -> RandomFlip In (horizontal_and_vertical)<br>
         -> RandomRotation etc.
   * By using data Augmentation we can incresse the size of our data set and get better results.

## 4. Model Creation :
   * Impliment state-of-art custom CNN architecture for model creation.
   * Use Convolution + Activation and Maxpooling layer , Adam optimizer are used.

## 5. Model Optimization :
   * By only using CNN layers we don't get good desire Accuracy, for this different Model optimization technique are implimented.<br>
     -> Add dropout Layers.<br>
     -> Add BatchNormalization Layers.<br>
     -> And EarlyStopping was used as callback function to reduse epochs size.<br>

## 6. Write Python Backend Server :

   * Write backend server to serve HTTP request from client . We used FastApi for model loading and make prediction.
   * Use Tf serving Using Docker as MLops operation , and load latent model by save_models folder.

## 7. Integrate Frontend with Backend :
   * Make User-Freindly Interface using streamlit framwork for provideing Input Image.
   * Integrate streanlit interface to Our Fastapi server and Predicting the output.

<br>
<br>

# Model Training Approach Notebook

Link : [Model Training Notebook](./Indian%20Medicinal%20Leaves%20Image%20Datasets/training.ipynb)

     

