# Pandas: Select the Rows where two Columns are Equal

import pandas as pd


df = pd.DataFrame({
    'A': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'B': [10, 20, 30, 50],
    'C': [10, 15, 30, 25],
})

print(df)

cols_equal = df.loc[(df['B'] == df['C'])]

print('-' * 50)

print(cols_equal)