import pandas as pd

df = pd.read_csv(r"C:\Users\gayathri\OneDrive\Documents\Desktop\apexplant-data-analytics\data\cleaned_superstore.csv")

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

df.to_excel("processed_data.xlsx", index=False)

print("Automation Completed Successfully")