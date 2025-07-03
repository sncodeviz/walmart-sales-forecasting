import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def main():
   df = pd.read_excel('Data_Files/Walmart_Sales.xlsx', sheet_name='Data')
   df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

   # Feature engineering
   df['Month'] = df['Date'].dt.month
   df['Year'] = df['Date'].dt.year

   # Define features and target
   X = df[['Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Month', 'Year']]
   y = df['Weekly_Sales']

   # Train-test split
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

   # Initialize and fit Random Forest model
   rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
   rf_model.fit(X_train, y_train)

   # Prediction
   y_pred = rf_model.predict(X_test)

   # Evaluation
   rmse = np.sqrt(mean_squared_error(y_test, y_pred))
   r2 = r2_score(y_test, y_pred)

   print("\nRandom Forest Regression Results:")
   print(f"RMSE: {rmse:.2f}")
   print(f"R-squared: {r2:.4f}")

if __name__ == '__main__':
   main()
