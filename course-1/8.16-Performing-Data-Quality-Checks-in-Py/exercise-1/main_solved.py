import pandas as pd

churn = pd.read_excel('customer_churn_dirty.xlsx')
churn['IsActiveMember'].value_counts()

"""
The ‘IsActiveMember’ column contains 
two types of binary identifiers: [1, 0] and [‘YES’, ‘NO’].
This needs to be rectified before the data can be used
for advanced analytics purposes.
"""
