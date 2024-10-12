# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone Project: Energy Consumption Forecasting

### Problem Statement

Utility companies or a households are trying to manage energy consumption efficiently. To achieve this, it's important to predict energy consumption accurately. This project goal to develop a time series regression model that forecasts global active power consumption based on historical data, time of day, and other relevant factors.

Long Short-Term Memory (LSTM) networks will be used to train the model; these networks can learn trends in energy use data and forecast the next time period (e.g., the next hour or day). The model's ability to create forecasts will be gauged for success using measures such as mean squared error (MSE) and mean absolute error (MAE).

This project is important because accurate energy consumption forecasting can help utility companies optimize energy distribution, reduce waste, and improve service quality. Households can also benefit by reducing their energy bills and environmental impact.

Developing a practical and effective energy consumption forecasting model can help contribute to a more sustainable and efficient energy management system.

---

### Data Dictionary

| Feature             | Type     | Description                                                                          |
| ------------------- | -------- | ------------------------------------------------------------------------------------ |
| DateTime            | datetime | The timestamp of the recorded data                                                   |
| Global_active_power | float    | The total active power consumed by the household (in kilowatts)                      |
| Year                | integer  | The year when the data was recorded                                                  |
| Quarter             | integer  | The quarter of the year when the data was recorded (1 = Jan-Mar, 4 = Oct-Dec)        |
| Month               | integer  | The month when the data was recorded (1 = January, 12 = December)                    |
| Day                 | integer  | The day of the month when the data was recorded (1 - 31)                             |
| Time_of_day         | integer  | The hour of the day when the data was recorded (0 - 23)                              |
| Day_of_week         | integer  | The day of the week when the data was recorded (1 = Monday, 7 = Sunday)              |
| Season              | integer  | The season when the data was recorded (1 = Spring, 2 = Summer, 3 = Fall, 4 = Winter) |

---

### Executive Summary

#### Data Collection

The following are the 2 datasets were used for this project, and collected using Python Reddit API Wrapper ([PRAW](https://praw.readthedocs.io/en/stable/)), 1000 posts were scraped for each datasets for `music` and `movies` subreddits. While scraping data, only data with non missing values for features `title` and `self_text` were collected, since these are important features for the model.

## Data Collected

**Datasets Collected**

- The dataset used for this project is the "Individual household electric power consumption" dataset, which can be downloaded [here](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption).

## Dataset Information

- **# Instances:** 2,075,259
- **# Features:** 9

Due to the large size of the dataset, it can be time-consuming to run analysis on the full dataset. A smaller sample can be used for testing and development purposes.

## Data Cleaning

The dataset contained various records of household power consumption. To ensure the data was clean and ready for analysis, I performed the following steps:

### Loading the Data

- Imported the dataset using appropriate libraries.
- Ensured the data was correctly loaded into a DataFrame.

### Handling Missing Values

- Checked for missing values in all columns.
- Dropped missing values since they represented only 1.25% of the datasets.

### Parsing Dates

- Combined the `Date` and `Time` columns into a single datetime column.
- Converted this combined column to a datetime format for easier time-series analysis.

### Data Type Conversion

- Ensured all columns had the correct data types, converting numerical columns from strings to floats/integers as needed.

### Resampling Data

- Resampled the data from minute to hourly to simplify the analysis and trends over time.

### Feature Engineering

- Created new features such as daily, weekly, and monthly aggregates to capture broader consumption patterns.
- Calculated rolling averages and moving windows to smooth out short-term fluctuations.

## Questions Explored

The cleaned data allowed to explore the following questions about household power consumption:

1. **What are the daily, weekly, and monthly trends in household power consumption?**

   - Analyzed how power usage varies over different time periods to identify peak and off-peak times.

2. **How does weather impact power consumption?**

   - Investigated the correlation between weather conditions or season (e.g., winter, spring, summer, and fall) and power usage.

3. **Can we predict future power consumption based on historical data?**

   - Applied time series forecasting models (e.g., ARIMA, LSTM) to predict future power usage and evaluate their accuracy.

4. **How do different models compare in forecasting power consumption?**
   - Compared the performance of various models to determine which one provides the most accurate and reliable forecasts.

The project aimed to provide insights into household power consumption patterns and improve prediction accuracy, which could be beneficial for energy management and planning.

#### Conclusion and Recommendations

##### Conclusions

- Accurately predicting household energy consumption is important for both utility companies and households to manage energy efficiently.
- The LSTM (time_step=50) model outperformed both ARIMA models (2,0,2) and (52,0,1), showing the lowest Mean Absolute Error (MAE) and Mean Squared Error (MSE) on both training and test sets.
- The consistent performance of the LSTM model suggests it generalizes well and is less likely to overfit compared to the ARIMA models, which showed significant differences between training and test errors.
- The ARIMA models, while useful, displayed higher test errors and potential overfitting, indicating they are less reliable for predicting new data.

##### Recommendations

- Utility companies should consider implementing the LSTM model for energy consumption forecasting to optimize energy distribution and reduce waste.
- Households can use predictions from the LSTM model to adjust their energy usage, potentially lowering their energy bills and environmental impact.
- Future work should focus on collecting more diverse data to enhance the model's robustness and accuracy across different regions and conditions.
- Continuous monitoring and updating of the model are recommended to adapt to changes in energy consumption patterns over time.

By using the LSTM model, stakeholders can benefit from more accurate energy consumption forecasts, leading to better energy management and sustainability.
