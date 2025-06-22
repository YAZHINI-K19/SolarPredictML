import joblib

# Load the saved solar calculator model from models folder
model = joblib.load('models/solar_calculator_model.pkl')

try:
    # Take user inputs
    load = float(input("Enter your energy load (in kWh): "))
    efficiency = float(input("Enter solar panel efficiency (%): "))
    hours_per_day = float(input("Enter sunlight hours per day: "))

    # Prepare input for prediction
    input_data = [[load, efficiency, hours_per_day]]

    # Predict number of solar panels needed
    prediction = model.predict(input_data)

    print(f"\nEstimated Number of Solar Panels Needed: {prediction[0]:.2f}")

except ValueError:
    print("Invalid input! Please enter valid numeric values.")
