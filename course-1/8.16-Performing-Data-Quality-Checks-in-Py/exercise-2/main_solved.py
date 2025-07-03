import pandas as pd
import re

churn = pd.read_excel('customer_churn_dirty.xlsx')

# Scan the 'EstimatedSalary' column for non-numeric characters
for x in churn['EstimatedSalary']:
    non_numeric = re.findall("[a-zA-Z]", str(x))
    if non_numeric:
        print(f"Non-numeric characters found in", x)
