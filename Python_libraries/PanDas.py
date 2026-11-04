import pandas as pd

people = pd.DataFrame({
    "Name": ["Dara" , "Lina"],
    "Age": [20, 21]
})

print(people)
print(people.shape)

from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
file = BASE / "data" / "student_scores.csv"

df = pd.read_csv(file)

# Always check what you have loaded before performing calculations
print(df.head()) #show sample records
print(df.shape) #shows the dimensions of the entire table
print(df.columns.tolist())

math = df["Math"] #One column: Series
selected = df[["Student", "Math"]] #Two columns: DataFrame

print(selected.shape)

mask = df["Math"] >= 80
print(mask.head().tolist())

math_80 = df.loc[mask, ["Student", "Math"]]
print(len(math_80))


#Calculate averages

#A. average for each subject
SUBJECTS = ["Math", "Science", "English"]
subject_names = df[SUBJECTS].mean()
print(subject_names.round(2))

#B. Average for each student
df["Average"] = df[SUBJECTS].mean(axis=1)
print(df.loc[0, "Average"])

#9. Sort and rank students
ranked = df.sort_values("Average", ascending=False)
print(ranked["Student"].head(3).tolist())

OUTPUT = BASE / "outputs"
OUTPUT.mkdir(exist_ok=True)
df.to_csv(OUTPUT / "analysis.csv", index=False)

print(df.isna().sum())

