import pandas as pd
import numpy as np
from statsmodels.tools.tools import add_constant
from statsmodels.stats.outliers_influence import variance_inflation_factor

def main():
   df = pd.read_excel('Data_Files/Walmart_Sales.xlsx', sheet_name='Data')

   # Convert 'Date' column to datetime format
   df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

   df['Month'] = df['Date'].dt.month
   df['Year'] = df['Date'].dt.year

   X = df[['Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Month', 'Year']]

   # Add constant (intercept) term for VIF calculation
   X = add_constant(X)

   # Calculate VIF for each feature
   vif_data = pd.DataFrame()
   vif_data["Feature"] = X.columns
   vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

   print("\nVariance Inflation Factor (VIF):")
   print(vif_data)

if __name__ == '__main__':
   main()
