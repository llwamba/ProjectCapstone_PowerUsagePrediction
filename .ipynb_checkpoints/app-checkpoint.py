 import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

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
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        df['DateTime'] = pd.to_datetime(df['DateTime'])

        st.write(df.head())

        scaler = MinMaxScaler(feature_range=(0, 1))
        scaler.fit(df[['Global_active_power']].values)
        scaled_data = preprocess_data(
            df[['Global_active_power']].values, scaler)

        time_step = st.sidebar.slider(
            "Time Step", min_value=1, max_value=50, value=50)

        X = create_sequences(scaled_data, time_step=time_step)
        print(X)

        X = X.reshape(X.shape[0], X.shape[1], 1)

        predictions = model.predict(X)
        predictions = scaler.inverse_transform(predictions)

        st.write("Predictions:")
        st.line_chart(predictions)


if __name__ == "__main__":
    main()
