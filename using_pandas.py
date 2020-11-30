import pandas as pd
col_list = ["Name", "Department"]
df = pd.read_csv("sample_file.csv", usecols=col_list)

print(df["Name"])
print(df["Department"])
 