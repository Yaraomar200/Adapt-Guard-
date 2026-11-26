import pandas as pd

path = r"C:\Users\yaram\SSF-Strategic-Selection-and-Forgetting\MachineLearningCVE\Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"

df = pd.read_csv(path)
df.columns = df.columns.str.strip()

print(df.shape)
print(df["Label"].value_counts())

print("--------------------------------")

import pandas as pd

path = r"C:\Users\yaram\SSF-Strategic-Selection-and-Forgetting\NSL_pre_data\PKDDTrain+.csv"

df = pd.read_csv(path)

print(df.shape)
print(list(df.columns))
print(df["labels5"].value_counts())