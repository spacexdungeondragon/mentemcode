import pandas as pd

churn = pd.read_excel('customer_churn_dirty.xlsx')

churn['Geography'].unique()
