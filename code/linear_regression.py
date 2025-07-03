import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def main():
   df = pd.read_excel('Data_Files/Walmart_Sales.xlsx', sheet_name='Data')

   # Convert 'Date' column to datetime format
   df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

   df['Month'] = df['Date'].dt.month
   df['Year'] = df['Date'].dt.year

   # Features and target
   X = df[['Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Month', 'Year']]
   y = df['Weekly_Sales']

   # Split data
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

   # Train model
   model = LinearRegression()
   model.fit(X_train, y_train)

   # Predict and evaluate
   y_pred = model.predict(X_test)
   rmse = np.sqrt(mean_squared_error(y_test, y_pred))
   r2 = r2_score(y_test, y_pred)

   print("\nLinear Regression Results:")
   print(f"RMSE: {rmse:.2f}")
   print(f"R-squared: {r2:.4f}")

if __name__ == '__main__':
   main()
