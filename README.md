# Time Series Forecasting Project: ARIMA & SARIMAX on ETH-USD Dataset

## 1. Project Overview

This project focuses on **time series modeling and forecasting** using historical **Ethereum (ETH) to USD price data**. The main objective is to build, evaluate, and compare **ARIMA** and **SARIMAX** models to understand price dynamics and generate short- to medium-term forecasts.

The project follows a **structured data science workflow**, starting from data understanding and preprocessing, through exploratory analysis, model development, diagnostics, forecasting, and evaluation.

---

## 2. Problem Statement

Cryptocurrency prices are highly volatile and influenced by trends, seasonality, and external factors. Accurate forecasting is challenging but valuable for:

* Investors and traders
* Risk management
* Market analysis and research

**Problem Definition:**

> Can historical ETH-USD price data be used to build reliable time series models that capture trends and seasonality and generate meaningful forecasts?

---

## 3. Project Objectives

The main objectives of this project are:

* To analyze the temporal behavior of ETH-USD prices
* To test and enforce stationarity in the time series
* To build and evaluate an **ARIMA** model for baseline forecasting
* To extend the model using **SARIMAX** to capture seasonality and exogenous effects
* To compare model performance using statistical metrics
* To generate and visualize future price forecasts

---

## 4. Dataset Description

### 4.1 Data Source

The dataset contains historical Ethereum price data against the US Dollar (ETH-USD).

### 4.2 Dataset Structure

Typical variables in the dataset include:

* **Date** – Trading date (time index)
* **Open** – Opening price
* **High** – Highest price of the day
* **Low** – Lowest price of the day
* **Close** – Closing price
* **Volume** – Trading volume

> The **Close price** is used as the primary target variable for time series modeling.

### 4.3 Time Frequency

* Daily observations
* Continuous time series with chronological ordering

---

## 5. Methodology

### 5.1 Data Preprocessing

Steps performed:

* Convert the date column to `datetime` format
* Set date as the time index
* Sort data chronologically
* Handle missing values (forward fill or removal)
* Select the target variable (Close price)

---

### 5.2 Exploratory Data Analysis (EDA)

EDA focuses on understanding the structure and behavior of the time series:

* Line plots to visualize trends and volatility
* Rolling mean and rolling standard deviation
* Seasonal decomposition (trend, seasonality, residuals)
* Identification of outliers and structural breaks

---

### 5.3 Stationarity Testing

Stationarity is essential for ARIMA-based models.

Tests applied:

* **Augmented Dickey-Fuller (ADF) Test**

Actions taken if non-stationary:

* Differencing (first or second order)
* Log transformation (if required)

---

## 6. Model Development

### 6.1 ARIMA Model

**ARIMA (p, d, q)** components:

* **p** – Autoregressive order
* **d** – Degree of differencing
* **q** – Moving average order

Model selection process:

* ACF and PACF plots
* Grid search using AIC/BIC criteria
* Residual diagnostics to confirm white noise behavior

Purpose:

* Serve as a baseline model
* Capture short-term dependencies and trends

---

### 6.2 SARIMAX Model

**SARIMAX (p, d, q) × (P, D, Q, s)** extends ARIMA by including:

* Seasonal components
* Exogenous variables (if available)

Key features:

* Captures repeating seasonal patterns
* Handles external regressors (e.g., volume, market indicators)

Seasonality:

* Determined using decomposition and domain knowledge
* Common seasonal periods tested (e.g., weekly or monthly cycles)

---

## 7. Model Evaluation

### 7.1 Train-Test Split

* Data split chronologically (no shuffling)
* Training set: historical data
* Test set: most recent observations

### 7.2 Evaluation Metrics

Models are compared using:

* **Mean Absolute Error (MAE)**
* **Root Mean Squared Error (RMSE)**
* **Mean Absolute Percentage Error (MAPE)**

Residual analysis:

* Autocorrelation of residuals
* Normality checks
* Ljung-Box test

---

## 8. Forecasting

Forecasting steps:

* Generate out-of-sample forecasts
* Visualize forecasts with confidence intervals
* Compare forecasts against actual values

Forecast horizon:

* Short-term (e.g., 7–30 days)
* Medium-term (e.g., 60–90 days)

---

## 9. Results and Discussion

This section discusses:

* Model performance comparison (ARIMA vs SARIMAX)
* Ability to capture trend and seasonality
* Forecast stability and uncertainty
* Limitations due to market volatility

Key insights:

* ARIMA performs well for short-term trends
* SARIMAX improves performance when seasonality is present
* Prediction uncertainty increases with longer horizons

---

## 10. Limitations

* Cryptocurrency markets are highly volatile
* External shocks are not fully captured
* Models rely solely on historical patterns
* Long-term forecasts should be interpreted cautiously

---

## 11. Future Improvements

Possible extensions include:

* Incorporating additional exogenous variables
* Using volatility models (ARCH/GARCH)
* Applying deep learning models (LSTM, GRU)
* Ensemble forecasting approaches
* Regime-switching time series models

---

## 12. Project Structure

```
├── data/
│   └── eth_usd_dataset.csv
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── eda.ipynb
│   ├── arima_model.ipynb
│   └── sarimax_model.ipynb
├── results/
│   ├── forecasts
│   └── evaluation_metrics
├── README.md
```

---

## 13. Tools and Technologies

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Statsmodels
* Scikit-learn
* Jupyter Notebook

---

## 14. Conclusion

This project demonstrates how classical time series models such as **ARIMA** and **SARIMAX** can be effectively applied to cryptocurrency price data. While these models have limitations in highly volatile markets, they provide strong baselines and valuable insights into temporal patterns and forecasting uncertainty.
