from pathlib import Path
import pandas as pd
import matplotlib
import sklearn

df = pd.read_csv(Path(__file__).resolve().parent / "data" / "study_scores.csv")
assert df.shape == (20, 3), "Restore the supplied dataset."
assert not df.isna().any().any(), "Use the original dataset without missing values."
print("Setup OK: Pandas, Matplotlib, and scikit-learn imported.")
print("Data OK: 20 records and 3 columns.")
