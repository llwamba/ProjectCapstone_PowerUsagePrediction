import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error

model = load_model('lstm_model.h5')


def preprocess_data(data, scaler):
    scaled_data = scaler.transform(data)
    return scaled_data


def create_sequences(data, time_step=1):
    X = []
    for i in range(len(data) - time_step + 1):
        X.append(data[i:(i + time_step), 0])
    return np.array(X)


def main():
    st.title("LSTM Model for Power Consumption Prediction")
    st.write(
        "The input CSV should have 50 rows of historic data and should be in the following format:")
    st.code("DateTime,Global_active_power\n8/15/2010 21:00,55.792")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df['DateTime'] = pd.to_datetime(df['DateTime'])

        if len(df) != 50:
            st.error("Error: The input CSV should have 50 rows of historic data.")
            return

        scaler = MinMaxScaler(feature_range=(0, 1))
        scaler.fit(df[['Global_active_power']].values)
        scaled_data = preprocess_data(
            df[['Global_active_power']].values, scaler)

        time_step = 50
        X = create_sequences(scaled_data, time_step=time_step)
        X = X.reshape(X.shape[0], X.shape[1], 1)
        predictions = model.predict(X)
        predictions = scaler.inverse_transform(predictions)

        last_date_time = df['DateTime'].iloc[-1]
        next_date_time = last_date_time + pd.Timedelta(hours=1)

        st.write("Next Date Time:", next_date_time)
        st.write("Next Predicted Power Consumption Value:",
                 predictions[-1][-1])

        actual_values = df['Global_active_power'].values[-len(predictions):]
        mse = mean_squared_error(actual_values, predictions)
        mae = mean_absolute_error(actual_values, predictions)

        st.write("Model Evaluation Metrics:")
        st.write("Mean Squared Error (MSE):", mse)
        st.write("Mean Absolute Error (MAE):", mae)


if __name__ == "__main__":
    main()
