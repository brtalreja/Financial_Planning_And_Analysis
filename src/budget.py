import pandas as pd
from utils import load_data, save_data

#Annual Budget Calculator
def calculate_budget(data):
    '''
        This function computes the annual budget per division based on the revenue and expense.
    '''
    data['Annual_Budget_Revenue'] = data.groupby('Division')['Revenue'].transform('sum') * 1.10 #10% Annual increase
    data['Annual_Budget_Expense'] = data.groupby('Division')['Expense'].transform('sum') * 1.05 #5% Annual increase
    data['Annual_Budget_Profit'] = data['Annual_Budget_Revenue'] - data['Annual_Budget_Expense']

    #We aggregate data here becuase budgeting is done on aggregated level rather than individual transactions.

    return data[['Division', 'Annual_Budget_Revenue', 'Annual_Budget_Expense', 'Annual_Budget_Profit']].drop_duplicates()

def main():
    data = load_data('../data/Elektronics_sales_data.csv')
    budget_data = calculate_budget(data)
    save_data(budget_data, '../data/Elektronics_budget_output.csv')

if __name__ == "__main__":
    main()

#COMMENT: We chose 5% and 10% becuase budgets are known to be based on historical performance and adjustments for the future.
# A 10% increase in revenue can be for achieveing some business growth objectives.
# While a 5% increase in expenses can be for planned investments and inflation.