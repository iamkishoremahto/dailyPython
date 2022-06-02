import pandas as pd
df= pd.read_csv('dirtydata.csv')
new_df= df.dropna()
print(new_df)