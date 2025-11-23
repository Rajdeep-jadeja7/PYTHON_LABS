#Task -1  Write a code snippet to check the data types of each column in a DataFrame.
import pandas as pd
df = pd.read_csv(r'D:\PYTHONLABS\Lab 20\sample_data.csv')
print(df.dtypes)

#TASK -2  Write a code snippet that demonstrates how to fill missing values with the mean of a column.

import pandas as pd
df = pd.read_csv(r'D:\PYTHONLABS\Lab 20\sample_data.csv')
print("Original Dataframe")
print(df)   
df = df.fillna(df.mean(numeric_only=True))
print("\nNew Dataframe after filling missiong values:")
print(df)
