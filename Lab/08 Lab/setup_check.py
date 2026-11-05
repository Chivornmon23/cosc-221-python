"""Run this before the lab."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib

base = Path(__file__).resolve().parent
data_file = base / "data" / "student_scores.csv"
assert data_file.exists(), "Extract the full folder, including data/."
df = pd.read_csv(data_file)
assert df.shape == (12, 5), "Use the original student_scores.csv."
print("Setup OK: NumPy, Pandas, and Matplotlib imported.")
print("Dataset OK: 12 records and 5 columns.")
