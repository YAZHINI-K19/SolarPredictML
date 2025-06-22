import joblib

# Load the saved model from the models folder
model = joblib.load('models/savings_estimator_model.pkl')

try:
    # Get user input
    energy_cost = float(input("Enter your energy cost: "))
    years = int(input("Enter number of years: "))
    tariff = float(input("Enter your tariff rate: "))
    
    # Prepare input for prediction
    input_data = [[energy_cost, years, tariff]]
    
    # Predict estimated savings
    prediction = model.predict(input_data)
    
    print(f"\nEstimated Savings over {years} years: ${prediction[0]:.2f}")
    
except ValueError:
    print("Invalid input! Please enter numeric values for energy cost, years, and tariff.")
