from pathlib import Path
import pandas as pd
import streamlit
df = pd.read_csv(Path(__file__).resolve().parent / "data/arcade_games.csv")
assert df.shape == (12, 4), "Restore the supplied CSV."
print("Setup OK: packages imported; 12 arcade games loaded.")
