# Air Quality Health Impact Prediction 🌍

## Overview
This project focuses on predicting the potential health impact based on various air quality indicators such as AQI, PM10, PM2.5, NO2, O3, and other environmental features. The model classifies the air quality impact into five categories: **Very High**, **High**, **Moderate**, **Low**, and **Very Low**. The project uses a **Random Forest** classifier and is integrated into a web-based interface using **Streamlit** for user interaction and real-time predictions.

---

## Project Components 🛠️

1. **Air Quality Prediction Model** 🌱:
   - A machine learning model built using the **Random Forest** algorithm.
   - The model is trained on a dataset containing information such as AQI, concentrations of particulate matter (PM10, PM2.5), gases (NO2, SO2, O3), temperature, humidity, wind speed, and hospital admissions.
   - The model is saved and deployed for predictions using a pickled file (`AirQuality.sav`).

2. **Streamlit Interface** 💻:
   - A user-friendly web application built using **Streamlit** that allows users to input air quality and environmental data.
   - After entering the data, users can predict the health impact based on the input features.
   - The predictions are displayed in real-time (e.g., "Very High", "High", "Moderate", "Low", "Very Low").

3. **Evaluation and Performance** 📊:
   - The model's performance is evaluated using classification metrics such as **precision**, **recall**, and **F1-score**. The model achieves an overall **accuracy** of 97%.
   - Different stages of the **Random Forest** model (imbalanced, balanced, with feature selection, and after hyper-parameter tuning) are compared using a bar chart to visualize performance.

---

## How to Use the Application 🚀

1. **Run the Streamlit App**:
   - Install required packages:
     ```bash
     pip install streamlit streamlit-lottie scikit-learn pickle5 pillow requests
     ```

   - Run the Streamlit app:
     ```bash
     streamlit run 1_🏠HomePage.py
     ```

2. **Enter Input Data** ✍️:
   - The user needs to enter the following inputs:
     - **AQI** (Air Quality Index)
     - Concentrations of particulate matter (PM10, PM2.5)
     - Concentrations of Nitrogen Dioxide (NO2), Sulphur Dioxide (SO2), Ozone (O3)
     - **Temperature** (in Celsius)
     - **Humidity** (in percentage)
     - **Wind Speed** (in m/s)
     - **Hospital Admissions Count**

3. **Receive Health Impact Prediction** 💡:
   - After entering the data, click on the **'Predict'** button to receive the health impact prediction:
     - **Very High**
     - **High**
     - **Moderate**
     - **Low**
     - **Very Low**

---

## Model Evaluation 📈

The **Random Forest** model was evaluated using different stages, including:
- **Imbalanced Dataset**
- **Balanced Dataset**
- **Feature Selection Applied**
- **Hyper-Parameter Tuning Applied**

The classification report shows excellent performance with the following metrics:

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0.0   | 0.94      | 0.93   | 0.94     | 1471    |
| 1.0   | 0.94      | 0.97   | 0.95     | 1376    |
| 2.0   | 1.00      | 0.97   | 0.98     | 1452    |
| 3.0   | 1.00      | 0.99   | 0.99     | 1464    |
| 4.0   | 0.98      | 1.00   | 0.99     | 1449    |
| **Accuracy** | **0.97** | | | **7212** |

---

## Sources 🔗

- [Dataset used for Machine Learning Model Building](https://www.kaggle.com/datasets/rabieelkharoua/air-quality-and-health-impact-dataset)

---

## Future Improvements 🔮
- Integrating more features for prediction, such as **weather conditions** and **real-time air quality data**.
- Optimizing the model using more advanced techniques like **deep learning**.

--- 