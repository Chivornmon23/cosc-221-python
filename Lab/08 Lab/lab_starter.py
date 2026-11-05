from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "outputs"
OUTPUT.mkdir(exist_ok=True)
SUBJECTS = ["Math", "Science", "English"]

# PART 1: NumPy (15 minutes)
scores = np.array([60, 70, 80, 90])
# TODO 1a: Print scores and scores.shape.
print(scores, scores.shape)
# TODO 1b: Print mean, minimum, and maximum.
print(scores.mean(), scores.min(), scores.max())
# TODO 1c: Add 5 to every score and print the result.
print(scores + 5)
# TODO 1d: Reshape scores into 2 rows and 2 columns, then print it.
print(scores.reshape(2, 2))

# PART 2: Read and inspect data (15 minutes)
df = pd.read_csv(BASE / "data" / "student_scores.csv")
# TODO 2a: Print the first 5 rows.
print(df.head())
# TODO 2b: Print the number of students and the shape of the DataFrame.
print(len(df), df.shape)
# TODO 2c: Print only the Student and Math columns.
print(df[["Student", "Math"]])

# PART 3: Summarize, filter, and sort (20 minutes)
# TODO 3a: Calculate and print subject_means for the three SUBJECTS.
subject_means = df[SUBJECTS].mean()
print(subject_means)
# TODO 3b: Create a new Average column using .mean(axis=1).
df["Average"] = df[SUBJECTS].mean(axis=1)
# TODO 3c: Select students whose Math score is at least 80. Print their
#          Student and Math columns, and print how many students match.
math_80 = df[df["Math"] >= 80]
print(math_80[["Student", "Math"]])
print(len(math_80))
# TODO 3d: Sort by Average from highest to lowest. Print the top 3.
print(df.sort_values("Average", ascending=False).head(3))
# TODO 3e: Save all 12 records, including Average, to outputs/analysis.csv.
df.to_csv(OUTPUT / "analysis.csv", index=False)

# PART 4: One clear chart (20 minutes)
# TODO 4a: Use subject_means to make a bar chart of the three subject means.
plt.bar(subject_means.index, subject_means.values)
# TODO 4b: Add a title and x/y labels. Set the score axis to 0-100.
plt.title("Subject Means")
plt.xlabel("Subject")
plt.ylabel("Mean Score")
plt.ylim(0, 100)
# TODO 4c: Save outputs/subject_means.png BEFORE calling plt.show().
plt.tight_layout()
plt.savefig(OUTPUT / "subject_means.png")
plt.show()

# PART 5: Independent change (10 minutes)
# TODO 5a: Find students whose Science score is at least 85.
#          Save their Student and Science columns to outputs/science_85.csv.
df[df["Science"] >= 85][["Student", "Science"]].to_csv(OUTPUT / "science_85.csv", index=False)
# TODO 5b: Complete reflections.txt in your own words.

print("Run finished. Check your TODOs and compare with the lab checkpoints.")