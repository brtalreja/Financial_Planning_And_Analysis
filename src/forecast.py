import pandas as pd
from utils import load_data, save_data

#Forecast Profit
def calculate_forecast(data):
    '''
        This function forecasts the profit based on the revenue and expense.
    '''
    data['Forecast_Revenue'] = data['Revenue'] * 1.05 #5% projected revenue
    data['Forecast_Expense'] = data['Expense'] * 1.03 #3% projected expense
    data['Forecast_Profit'] = data['Forecast_Revenue'] - data['Forecast_Expense']

    #We do not use groupby here becuase forecasting is generally done on a more detailed level. Grouping those by division and aggregating the data will loose its granularity.

    return data

def main():
    data = load_data('../data/Elektronics_sales_data.csv')
    forecast_data = calculate_forecast(data)
    save_data(forecast_data, '../data/Elektronics_forecast_output.csv')

if __name__ == "__main__":
    main()

#COMMENT: As a general concept, revenue and expense grow over time due to various factors, including market growth, inflation, and operational efficiency.
# Applying a growth factor helps estimate the future values based on these historical trends.

#Example: 5% taken here to account for a moderate growth rate and 3%  a slightly lower rate to account for inflation or minor expenses.