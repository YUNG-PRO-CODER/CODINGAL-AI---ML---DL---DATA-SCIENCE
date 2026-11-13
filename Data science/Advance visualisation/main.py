#import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
sns.set_theme(style="whitegrid", palette="deep")

print("FIRST 5 ROWS:")
print(tips.head())

print("\nDATASET INFORMATION:")
print(tips.info())

print("\nSTATISTICAL SUMMARY:")
print(tips.describe())

plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x="day", y="tip", errorbar=None)
plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip ($)")
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(data=tips, x="day", hue="day", legend=False)
plt.title("Number of Customers by Day")
plt.xlabel("Day")
plt.ylabel("Customer Count")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()

plt.figure(figsize=(8, 5))
sns.stripplot(data=tips, x="day", y="total_bill", jitter=True, alpha=0.6)
plt.title("Individual Restaurant Bills")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()

plt.figure(figsize=(8, 5))
sns.swarmplot(data=tips, x="day", y="tip", size=4)
plt.title("Distribution of Tips by Day")
plt.xlabel("Day")
plt.ylabel("Tip ($)")
plt.show()

sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter", height=7)
plt.show()

sns.pairplot(data=tips, vars=["total_bill", "tip", "size"], hue="sex")
plt.show()

plt.figure(figsize=(8, 5))
sns.pointplot(data=tips, x="time", y="tip", hue="sex", errorbar=None)
plt.title("Average Tip by Time and Gender")
plt.xlabel("Meal Time")
plt.ylabel("Average Tip ($)")
plt.show()

sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex", height=6, aspect=1.3)
plt.title("Restaurant Bill vs Tip")
plt.show()

print("\nRestaurant Bill Explorer completed!")