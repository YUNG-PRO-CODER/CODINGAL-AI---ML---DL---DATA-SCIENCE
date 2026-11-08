
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
df = df.dropna()

print("\n========== DATASET HEAD ==========")
print(df.head())

print("\n========== DATASET INFORMATION ==========")
df.info()

print("\n========== DATASET DESCRIPTION ==========")
print(df.describe())

print("\n========== UNIQUE SPECIES ==========")
print(df["species"].unique())

print("\n========== UNIQUE ISLANDS ==========")
print(df["island"].unique())

sns.histplot(data=df, x="body_mass_g", bins=20, color="steelblue")

plt.title("Penguin Body Mass Distribution")
plt.xlabel("Body Mass (g)")
plt.ylabel("Frequency")
plt.show()

sns.histplot(data=df, x="flipper_length_mm", bins=10)
plt.title("Flipper Length - 10 Bins")
plt.show()

sns.histplot(data=df, x="flipper_length_mm", bins=30)
plt.title("Flipper Length - 30 Bins")
plt.show()


sns.kdeplot(data=df, x="flipper_length_mm", hue="species",fill=True)

plt.title("Flipper Length Distribution by Species")
plt.xlabel("Flipper Length (mm)")
plt.show()

sns.histplot(data=df, x="flipper_length_mm", kde=True, color="coral")

plt.title("Flipper Length Distribution")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Frequency")
plt.show()

sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species")

plt.title("Flipper Length vs Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()

sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="island")

plt.title("Flipper Length vs Body Mass by Island")
plt.show()

sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species")

plt.title("Bill Length vs Bill Depth")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.show()

corr = df.corr(numeric_only=True)

print("\n========== CORRELATION MATRIX ==========")
print(corr)

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Penguin Features Correlation Heatmap")
plt.show()



corr_pairs = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool)).stack()

strongest = corr_pairs.abs().idxmax()
weakest = corr_pairs.abs().idxmin()

print("\n========== STRONGEST CORRELATION ==========")
print(strongest, corr_pairs[strongest])

print("\n========== WEAKEST CORRELATION ==========")
print(weakest, corr_pairs[weakest])

print("\n================================")
print("SEABORN PRACTICAL COMPLETED!")
print("================================")
