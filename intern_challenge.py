# Alexia Pittas
# saved the Winter Data Sciene Intern Challenge Data Set as a csv in the same folder as this .py file'intern_data.csv'
# question 1 part c

import pandas as pd

df = pd.read_csv('intern_data.csv')

pd.set_option('display.max_columns', None)
print(df) #checking that the file read

#calculating the median value of order amount
median = df['order_amount'].median()

print('Median Order Amount: ' + str(median))

