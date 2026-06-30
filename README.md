# Algerian Forest Fire Prediction using Machine Learning

An end-to-end Machine Learning project that predicts the **Fire Weather Index (FWI)** using meteorological observations from the Algerian Forest Fires dataset. The project demonstrates the complete ML workflow including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and deployment through a Flask web application.

---

## Project Overview

The Fire Weather Index (FWI) is an indicator used to estimate wildfire risk based on weather conditions. This project uses historical weather observations to train a machine learning regression model capable of predicting the FWI for new environmental conditions.

The application allows users to enter weather parameters through a web interface and instantly receive the predicted Fire Weather Index.

---

## Features

- End-to-end Machine Learning workflow
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Scaling using StandardScaler
- Multiple Regression Model Training
- Model Performance Evaluation
- Best Model Selection
- Model Serialization using Pickle
- Interactive Flask Web Application
- Modern Responsive User Interface
- Input Validation using dataset value ranges

---

## Dataset

**Dataset:** Algerian Forest Fires Dataset

The dataset contains meteorological observations collected from two regions in Algeria.

- Bejaia Region
- Sidi Bel-Abbes Region

### Input Features

| Feature | Description |
|----------|-------------|
| Temperature | Air Temperature (°C) |
| RH | Relative Humidity (%) |
| Ws | Wind Speed (km/h) |
| Rain | Rainfall (mm) |
| FFMC | Fine Fuel Moisture Code |
| DMC | Duff Moisture Code |
| ISI | Initial Spread Index |
| Classes | Fire / Not Fire |
| Region | Region Identifier |

### Target Variable

- Fire Weather Index (FWI)

---

# Machine Learning Workflow

### 1. Data Collection

- Load the Algerian Forest Fires dataset

### 2. Data Preprocessing

- Handle missing values
- Remove unnecessary columns
- Convert categorical variables
- Data cleaning

### 3. Exploratory Data Analysis

- Correlation Analysis
- Feature Relationships
- Data Distribution
- Outlier Detection

### 4. Feature Engineering

- Feature Selection
- Train-Test Split
- Standardization using StandardScaler

### 5. Model Training

The following regression models were trained and evaluated:

- Linear Regression
- Lasso Regression
- Ridge Regression
- ElasticNet Regression
- RidgeCV
- ElasticNetCV

After evaluation, **Ridge Regression** was selected as the final model.

### 6. Model Deployment

- Save trained model using Pickle
- Save StandardScaler
- Build Flask application
- Predict Fire Weather Index through web interface

---

# Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-learn

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib
- Seaborn

## Web Framework

- Flask

## Development Tools

- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

---

# Project Structure

```
Algerian-Forest-Fire-Prediction
│
├── application.py
├── requirements.txt
├── README.md
│
├── models
│   ├── ridge.pkl
│   └── scaler.pkl
│
├── notebooks
│   ├── cleaning_algerian.ipynb
│   ├── modeltraining.ipynb
│   └── Algerian_forest_fire_cleaned_dataset.csv
│
├── templates
│   ├── index.html
│   └── form.html
│
└── static
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/iamvrvasanth/Algerian-Forest-Fire-Prediction.git
```

Move to the project directory

```bash
cd Algerian-Forest-Fire-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python application.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# Application Workflow

```
User Input
      │
      ▼
Input Validation
      │
      ▼
Feature Scaling
      │
      ▼
Ridge Regression Model
      │
      ▼
Predicted Fire Weather Index
      │
      ▼
Display Result
```

---

# Screenshots

## Home Page

Add a screenshot here.

---

## Prediction Form

Add a screenshot here.

---

## Prediction Result

Add a screenshot here.

---

# Learning Outcomes

This project helped strengthen my understanding of:

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Feature Scaling
- Regression Algorithms
- Model Evaluation
- Model Serialization
- Flask Application Development
- HTML & CSS Integration
- Git and GitHub Workflow

---

# Future Enhancements

The following improvements are planned for future versions of the project:

- Deploy the application on AWS EC2 or Render
- Store datasets and trained models in Amazon S3
- Build an automated data pipeline for preprocessing and model retraining
- Integrate GitHub Actions for CI/CD
- Containerize the application using Docker
- Compare additional machine learning algorithms
- Add interactive visualizations using Plotly
- Store prediction history in a database
- Deploy the model using cloud-based inference services

---

# Requirements

- Python 3.10+
- Flask
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# Repository

```
Algerian Forest Fire Prediction using Machine Learning
```

GitHub Repository

```
https://github.com/iamvrvasanth/Algerian-Forest-Fire-Prediction
```

---

# Author

**Vasanth V R**

Computer Engineering Student

GitHub

https://github.com/iamvrvasanth

LinkedIn

https://www.linkedin.com/in/vasanth-v-r/

---

# License

This project is developed for educational purposes and serves as a portfolio project demonstrating an end-to-end machine learning workflow using Python, Scikit-learn, and Flask.
