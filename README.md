# House-price-prediction
# 🏠 Housing Price Prediction

A machine learning project that predicts median housing prices in California using data from the 1990 census. This project uses both **Linear Regression** and **Random Forest** models for regression analysis.

---

## 📌 Project Overview

This project uses the `housing.csv` dataset to train and evaluate models that predict the **median house value** based on features like population, income, and location proximity to the ocean.

Key steps include:
- Data cleaning and preprocessing
- Feature engineering
- One-hot encoding of categorical variables
- Training Linear Regression and Random Forest models
- Comparing model performances using RMSE and R² score

---

## 📂 Dataset: `housing.csv`

| Feature               | Description                                      |
|------------------------|--------------------------------------------------|
| `longitude`            | Longitude of the district                        |
| `latitude`             | Latitude of the district                         |
| `housing_median_age`   | Median age of houses in the district             |
| `total_rooms`          | Total number of rooms                            |
| `total_bedrooms`       | Total number of bedrooms                         |
| `population`           | Total population                                 |
| `households`           | Number of households                             |
| `median_income`        | Median income of the population                  |
| `ocean_proximity`      | Location category (e.g., NEAR BAY, INLAND)       |
| `median_house_value`   | **Target**: Median house value in USD            |

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn
- Jupyter Notebook

---

