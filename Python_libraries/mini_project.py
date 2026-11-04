
import numpy as np
import pandas as pd
from pathlib import Path

# 1. Create the dataset
data = {
    "Student": ["Dara", "Lina", "Sopheak", "Rith", "Maly", "Sori"],
    "Math": [65, 78, 92, 85, 55, 80],
    "Science": [70, 82, 88, 90, 60, 75],
    "English": [60, 75, 90, 95, 70, 85]
}

df = pd.DataFrame(data)

# 2. Inspect the dataset
print("First five rows:")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

# 3. Use NumPy for numerical analysis
math_scores = np.array(df["Math"])

print("Math mean:", np.mean(math_scores))
print("Highest Math score:", np.max(math_scores))
print("Lowest Math score:", np.min(math_scores))

# 4. Select columns and filter rows
print("\nStudent names and Math scores:")
print(df[["Student", "Math"]])

print("\nStudents with Math >= 80:")
print(df.loc[df["Math"] >= 80, ["Student", "Math"]])

# 5. Calculate subject and student averages
subjects = ["Math", "Science", "English"]

print("\nSubject averages:")
print(df[subjects].mean(axis=0).round(2))

df["Average"] = df[subjects].mean(axis=1)

# 6. Sort by average
ranked = df.sort_values("Average", ascending=False)

print("\nRanked students:")
print(ranked[["Student", "Average"]])

print("\nTop three:")
print(ranked["Student"].head(3).tolist())

# 7. Export to CSV
BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "outputs"
OUTPUT.mkdir(exist_ok=True)

df.to_csv(OUTPUT / "analysis.csv", index=False)

print("\nAnalysis saved to outputs/analysis.csv")
