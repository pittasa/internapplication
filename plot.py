#Alexia Pittas
#Supporting work for question 1 part a

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('intern_data.csv')

mean= df['order_amount'].mean()
print(mean)
median = df['order_amount'].median()
print(median)

res = sns.violinplot(df['order_amount'])
plt.show()