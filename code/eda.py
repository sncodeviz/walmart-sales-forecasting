import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
   df = pd.read_excel('Data_Files/Walmart_Sales.xlsx', sheet_name='Data')

   # Convert 'Date' column to datetime format
   df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

   print(df.head())

   # Descriptive Statistics
   columns_to_analyze = ['Weekly_Sales', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
   for col in columns_to_analyze:
       print(f"\nDescriptive Statistics for: {col}")
       mean_val = np.mean(df[col])
       print(f"Mean = {mean_val:.2f}")

       std_val = np.std(df[col])
       print(f"Standard Deviation = {std_val:.2f}")

       median_val = np.median(df[col])
       print(f"Median = {median_val:.2f}")

       dfree = len(df[col]) - 1
       print(f"Degree of Freedom = {dfree}")

       min_val = np.min(df[col])
       print(f"Minimum = {min_val:.2f}")

       max_val = np.max(df[col])
       print(f"Maximum = {max_val:.2f}")

       freq = df[col].value_counts().head(5)
       print("Top 5 Frequencies:")
       print(freq)

   # Histograms (key features only)
   features_hist = ['Weekly_Sales', 'Temperature']

   for col in features_hist:
       plt.figure(figsize=(8, 5))
       sns.histplot(df[col], bins=30, kde=True)
       plt.title(f'Distribution of {col}')
       plt.xlabel(col)
       plt.ylabel('Frequency')
       plt.grid(True)
       plt.tight_layout()
       plt.show()

   # Boxplots (key features only)
   features_box = ['Weekly_Sales', 'Fuel_Price']

   for col in features_box:
       plt.figure(figsize=(8, 5))
       sns.boxplot(x=df[col])
       plt.title(f'Boxplot of {col}')
       plt.tight_layout()
       plt.show()

if __name__ == '__main__':
   main()
