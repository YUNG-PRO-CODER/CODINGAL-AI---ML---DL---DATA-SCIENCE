
import numpy as np
import pandas as pd

scores = np.array([950, 870, 780, 650, 540], dtype=np.int64)
players = ["Atharv", "Rahul", "Arjun", "Rohan", "Karan"]  # ts is the code
series = pd.Series(scores, index=players)

print("\nPANDAS SERIES")
print(series)

data = {
    "Player": ["Atharv", "Rahul", "Arjun", "Rohan", "Karan"],
    "Level": np.array([10, 9, 8, 7, 6]),
    "Score": np.array([950, 870, 780, 650, 540]),
    "Wins": np.array([25, 20, 18, 15, 10])
}

df = pd.DataFrame(data)

print("\nDATAFRAME")
print(df)


print("\nLOC")

print("Top player's row:")
print(df.loc[0])

print("\nRows 2 and 3:")
print(df.loc[2:3])

full_df = pd.read_csv("Data science\Intro to Pandas\leaderboard.csv")

print("\nCSV DATA")

print(full_df.head())

print(full_df.tail(3))

full_df.info()


print("\nDROPNA")

clean_df = full_df.dropna()
print(clean_df)

print("\nFILLNA")

filled_df = full_df.fillna(0)
print(filled_df)


print("\nSTATISTICS")

numeric_scores = full_df["Score"].dropna().to_numpy()

print("Scores:", numeric_scores)
print("Total:", np.sum(numeric_scores))
print("Average:", np.mean(numeric_scores))
print("Highest:", np.max(numeric_scores))
print("Lowest:", np.min(numeric_scores))
