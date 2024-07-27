#Import required libraries.
import pandas as pd
import numpy as np

#Setting the seed.
np.random.seed(42)

#Generate synthetic data.
num_rows = 5000
divisions = ['North', 'South', 'East', 'West']
products = ['Smartphones', 'Laptops', 'Tablets', 'Smartwatches', 'Headphones', 'Speakers']

data = {
    'Month' : np.random.choice(pd.date_range('2023-01-01', '2023-12-01', freq = 'MS').strftime('%Y-%m'), num_rows),
    'Division' : np.random.choice(divisions, num_rows),
    'Product' : np.random.choice(products, num_rows),
    'Revenue': np.random.uniform(50000, 200000, num_rows),
    'Expense': np.random.uniform(30000, 150000, num_rows),
    'Employee_Count': np.random.randint(10, 100, num_rows),
    'Customer_Count': np.random.randint(100, 1000, num_rows),
    'New_Customers' : np.random.randint(5, 50, num_rows),
    'Lost_Customers' : np.random.randint(1, 20, num_rows),
    'Ad_Spend': np.random.uniform(1000, 10000, num_rows),
    'IT_Spend': np.random.uniform(5000, 20000, num_rows),
    'R&D_Spend': np.random.uniform(10000, 50000, num_rows),
    'Profit': np.random.uniform(10000, 80000, num_rows),
}

df = pd.DataFrame(data)
df.to_csv('../data/Elektronics_sales_data.csv', index=False)