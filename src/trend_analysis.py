import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import load_data, save_data

def calculate_trends(data):
    '''
        This fucntion is used to calculate the percentage change in revenue, expense, and profit for each division.
    '''
    data['Revenue_Growth'] = data.groupby('Division')['Revenue'].pct_change()
    data['Expense_Growth'] = data.groupby('Division')['Expense'].pct_change()
    data['Profit_Growth'] = data.groupby('Division')['Profit'].pct_change()

    return data

def plot_yearly_trends(data):
    '''
        Plot the yearly growth trends for revenue, expense, and profit for each division.
    '''
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    yearly_data = data.groupby(['Year', 'Division'], as_index=False)[numeric_columns].mean()
    
    plt.figure(figsize=(10, 6))
    for division in yearly_data['Division'].unique():
        division_data = yearly_data[yearly_data['Division'] == division]
        plt.plot(division_data['Year'], division_data['Revenue_Growth'], marker='s', label=f'{division} Revenue Growth')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate')
    plt.title('Yearly Revenue Growth Trends by Division')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../data/revenue_trend_analysis.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    for division in yearly_data['Division'].unique():
        division_data = yearly_data[yearly_data['Division'] == division]
        plt.plot(division_data['Year'], division_data['Expense_Growth'], marker='s', label=f'{division} Expense Growth')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate')
    plt.title('Yearly Expenses Growth Trends by Division')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../data/expense_trend_analysis.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    for division in yearly_data['Division'].unique():
        division_data = yearly_data[yearly_data['Division'] == division]
        plt.plot(division_data['Year'], division_data['Profit_Growth'], marker='s', label=f'{division} Profit Growth')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate')
    plt.title('Yearly Profit Growth Trends by Division')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../data/profit_trend_analysis.png')
    plt.show()

def main():
    data = load_data('../data/Elektronics_sales_data.csv')
    
    trend_data = calculate_trends(data)
    
    save_data(trend_data, '../data/Elektronics_trend_data.csv')
    
    plot_yearly_trends(trend_data)

if __name__ == "__main__":
    main()

#COMMENT: 

# The trend analysis reveals the yearly growth patterns for key financial and operational metrics across different divisions (East, West, North, and South) over the period from 2010 to 2024.
# Revenue growth trends vary significantly across divisions. Some divisions show steady growth, while others exhibit volatility with occasional declines. This could be due to market conditions, competitive pressures, or division-specific strategies.
# Expense growth trends mirror the revenue trends to some extent. However, in some divisions, expenses grow at a faster rate than revenue, indicating potential inefficiencies or increased investment in growth areas.
# Profit growth trends are directly influenced by the revenue and expense growth trends. Divisions with controlled expenses relative to revenue show better profit growth. Volatility in profit growth may indicate inconsistent performance or external factors affecting profitability.
