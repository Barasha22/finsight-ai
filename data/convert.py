import pandas as pd

df = pd.read_excel('data/financial_sample.xlsx')
df.to_csv('data/financial_sample.csv', index=False)
print("Done converting Excel to CSV: ", len(df), "rows converted.")
print(df.columns.tolist())