
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Category": ["Electronics", "Clothing", "Furniture", "Electronics"],
    "Sales": [5000, 2000, 3000, 8000],
    "Cost": [3000, 1000, 2500, 5000]
}

df = pd.DataFrame(data)

df["Profit"] = df["Sales"] - df["Cost"]

print("Retail Business Analysis")
print(df)
print("\nCategory-wise Profit:")
print(df.groupby("Category")["Profit"].sum())

df.groupby("Category")["Profit"].sum().plot(kind="bar")
plt.title("Category-wise Profit")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

print("\nProject Completed Successfully!")
