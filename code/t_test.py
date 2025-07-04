import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

def main():
   df = pd.read_excel('Data_Files/Walmart_Sales.xlsx', sheet_name='Data')

   # Convert 'Date' column to datetime format
   df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

   holiday_sales = df[df['Holiday_Flag'] == 1]['Weekly_Sales']
   non_holiday_sales = df[df['Holiday_Flag'] == 0]['Weekly_Sales']

   # Two-sample t-test (unequal variances = Welch's t-test)
   t_stat, p_val = ttest_ind(holiday_sales, non_holiday_sales, equal_var=False)

   print("Two-Sample T-Test Results:")
   print(f"T-statistic: {t_stat:.4f}")
   print(f"P-value: {p_val:.4f}")

   alpha = 0.05
   if p_val < alpha:
       print("Result: Reject the null hypothesis. Sales are significantly different on holiday weeks.")
   else:
       print("Result: Fail to reject the null hypothesis. No significant difference in sales.")

if __name__ == '__main__':
   main()
