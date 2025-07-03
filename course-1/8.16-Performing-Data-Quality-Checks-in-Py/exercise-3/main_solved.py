import pandas as pd

churn = pd.read_excel('customer_churn_dirty.xlsx')

for x in churn['Satisfaction Score']:
    invalid = (x % 1 != 0)
    if invalid or x < 1 or x > 5:
        print(f"Invalid value found in Satisfaction Score:", x)
