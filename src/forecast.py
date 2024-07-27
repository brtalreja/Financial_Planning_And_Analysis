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

    return data

def main():
    data = load_data('../data/Elektronics_sales_data.csv')
    forecast_data = calculate_forecast(data)
    save_data(forecast_data, '../data/Elektronics_forecast_output.csv')

if __name__ == "__main__":
    main()