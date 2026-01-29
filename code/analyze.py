import pandas as pd

df = pd.read_csv("../data/sales.csv")
df.describe().to_csv("../data/summary.csv")

print("Done")

