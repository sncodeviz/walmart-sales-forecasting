import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
   df = pd.read_excel('Data_Files/Walmart_Sales.xlsx', sheet_name='Data')

   # Convert 'Date' column to datetime format
   df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

   print(df.head())

if __name__ == '__main__':
   main()
