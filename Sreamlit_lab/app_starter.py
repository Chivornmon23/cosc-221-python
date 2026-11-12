from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Arcade Night", page_icon="🎮", layout="centered")
BASE = Path(__file__).resolve().parent
CATEGORIES = ["All", "Action", "Racing", "Puzzle"]
try:
    df = pd.read_csv(BASE / "data" / "arcade_games.csv")
except (FileNotFoundError, pd.errors.ParserError, pd.errors.EmptyDataError):
    st.error("Cannot read the game list. Extract the complete lab folder again.")
    st.stop()
if not set(["Game", "Category", "Tokens", "Rating"]).issubset(df.columns):
    st.error("Unexpected columns. Restore arcade_games.csv.")
    st.stop()

st.title("Arcade Night")
st.subheader("Find your next game")
st.text("Plan a game night with fictional arcade games. Choose a category and token budget.")
st.info("The budget is for one play of one game. Ratings are fictional and out of 5.")

category = st.selectbox("Game category", CATEGORIES)
budget = st.slider("Maximum tokens per game", 0, 10, 6)
filtered = df.copy()

if category != "All":
    filtered = filtered[filtered["Category"] == category]
filtered = filtered[filtered["Tokens"] <= budget]

st.metric("Games available", len(filtered))
if filtered.empty:
    st.warning("No games fit yet. Add more tokens or choose another category.")
else:
    mean_rating = filtered["Rating"].mean()
    st.metric("Mean player rating", f"{mean_rating:.2f}/5")

st.subheader("Games you can play")
st.dataframe(filtered, hide_index=True)
if not filtered.empty:
    st.subheader("Compare player ratings")
    chart_data = filtered.set_index("Game")[["Rating"]]
    st.bar_chart(chart_data)
st.caption("Pick a game you would play and explain your choice to a classmate.")