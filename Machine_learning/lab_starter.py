"""Linear regression lab: complete one part at a time, then run this saved script.
Run: python lab_starter.py
The checkpoints stop cleanly until you replace the None values with your code.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "outputs"
OUTPUT.mkdir(exist_ok=True)
df = pd.read_csv(BASE / "data" / "study_scores.csv")

# PART 1: Inspect.
# TODO 1: Print df.head(), df.shape, and df.isna().sum().
print(df.head())
print(df.shape)
print(df.isna().sum())

# Check: 20 records, 3 columns, and no missing values.

# PART 2: Prepare and split.
X = df[["StudyHours"]]  # TODO 2a: A DataFrame containing only StudyHours (double brackets).
y = df["ExamScore"]  # TODO 2b: A Series containing ExamScore (single brackets).
if X is None or y is None:
    print("Complete Part 2a-2b, save, and run again.")
    raise SystemExit(0)

# Split code is supplied. Do not change test_size or random_state.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
print("Training records:", len(X_train))
print("Test records:", len(X_test))

# PART 3: Train and predict.
model = LinearRegression()  # TODO 3a: Create a LinearRegression instance.
if model is None:
    print("Complete Part 3a, save, and run again.")
    raise SystemExit(0)
model.fit(X_train, y_train) # TODO 3b: Fit model using X_train and y_train ONLY.
y_pred = model.predict(X_test)  # TODO 3c: Predict the scores for X_test.
if y_pred is None:
    print("Complete Part 3b-3c, save, and run again.")
    raise SystemExit(0)

# PART 4: Evaluate.
mae = mean_absolute_error(y_test, y_pred)  # TODO 4a: mean_absolute_error(y_test, y_pred).
if mae is None:
    print("Complete Part 4a, save, and run again.")
    raise SystemExit(0)

# Baseline comparison and export are supplied. Read these lines.
baseline_predictions = [y_train.mean()] * len(y_test)
baseline_mae = mean_absolute_error(y_test, baseline_predictions)
comparison = pd.DataFrame({
    "StudyHours": X_test["StudyHours"],
    "Actual": y_test,
    "Predicted": y_pred,
})
comparison["AbsoluteError"] = (
    comparison["Actual"] - comparison["Predicted"]
).abs()
print(comparison.round(2))
print(f"Model MAE: {mae:.2f} score points")
print(f"Baseline MAE: {baseline_mae:.2f} score points")
comparison.to_csv(OUTPUT / "test_predictions.csv", index=False)

# PART 5: Plot.
plt.figure(figsize=(10, 3.4))
# TODO 5a: Scatter X_train["StudyHours"] against y_train; label Training data.
plt.scatter(
    X_train["StudyHours"],
    y_train,
    label="Training data"
)
# TODO 5b: Scatter X_test["StudyHours"] against y_test; use marker="x".
plt.scatter(X_test["StudyHours"],
            y_test,
            marker="x",
            label="Test data"
            )
line_x = pd.DataFrame({"StudyHours": [1.0, 10.5]})
# TODO 5c: Plot line_x["StudyHours"] against model.predict(line_x).
#          Use color="red" and label="Fitted line".
plt.plot(
    line_x["StudyHours"],
    model.predict(line_x),
    color="red",
    label="Fitted line"
)
# TODO 5d: Add title, axis labels, 0-100 y limits, legend, tight_layout.
plt.title("Fictional study hours and exam scores.")
plt.xlabel("Study hours")
plt.ylabel("Exam score (out of 100")
plt.ylim(0, 100)
plt.legend()
plt.tight_layout()
# TODO 5e: Save OUTPUT / "regression_plot.png" before plt.show().
plt.savefig(
    OUTPUT/ "regression_plot.png",
    dpi=150
)
# PART 6: New input and short report.
new_input = pd.DataFrame({"StudyHours": [6.0]})
new_score = model.predict(new_input)[0]  # TODO 6a: model.predict(new_input)[0].
if new_score is not None:
    # Report writing is supplied; it uses your computed results.
    report = (
        f"Training records: {len(X_train)}\n"
        f"Test records: {len(X_test)}\n"
        f"Model MAE: {mae:.2f} score points\n"
        f"Baseline MAE: {baseline_mae:.2f} score points\n"
        f"Prediction for 6.0 hours: {new_score:.2f}\n"
        "Fictional data: classroom demonstration only.\n"
    )
    print(report)
    (OUTPUT / "metrics.txt").write_text(report, encoding="utf-8")
else:
    print("Complete Part 6a to generate metrics.txt.")
# TODO 6b: Complete reflections.txt and test_checklist.txt.
# Supplied: show a window only after a plot has been added.
if plt.gca().has_data():
    plt.show()
plt.close()

