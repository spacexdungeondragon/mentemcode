# Import pandas library
import pandas as pd

cars = pd.read_csv('cars.csv')

# Perform one-hot encoding on the 'ownership' column
encoded_ownership = pd.get_dummies(cars['ownership'], prefix='ownership')

# Concatenate the original data frame with the one-hot encoded data frame
cars_encoded = pd.concat([cars, encoded_ownership], axis=1)
