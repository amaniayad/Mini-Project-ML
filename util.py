# Import necessary libraries
import pickle
import numpy as np
import joblib
import pandas as pd


def predict_delay(month, day_of_month, day_of_week, dep_time, unique_carrier, origin, dest, distance):
    try:
        # Create a DataFrame for the new data
        new_data = pd.DataFrame({
            'Month': [month],
            'DayOfMonth': [day_of_month],
            'DayOfWeek': [day_of_week],
            'DepTime': [dep_time],
            'UniqueCarrier': [unique_carrier],
            'Origin': [origin],
            'Dest': [dest],
            'Distance': [distance]
        })

        # Load the saved scaler, encoder, and model
        loaded_scaler = joblib.load('scaler.pkl')
        loaded_ordinal_encoder = joblib.load('encoder.pkl')
        loaded_propagation_model = joblib.load('svm_model.pkl')

        # Encode categorical features
        categorical_columns = ['UniqueCarrier', 'Origin', 'Dest']
        new_data[categorical_columns] = loaded_ordinal_encoder.transform(new_data[categorical_columns])

        # Scale all features
        for col in new_data.columns:
            new_data[col] = loaded_scaler.transform(new_data[col].values.reshape(-1, 1))

        # Prepare the input for prediction
        prediction_input = new_data.values.reshape(1, -1)

        # Make the prediction using the loaded model
        delay_prediction = loaded_propagation_model.predict(prediction_input)[0]

        return delay_prediction

    except KeyError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    print('hello')
