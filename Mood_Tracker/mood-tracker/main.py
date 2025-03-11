import streamlit as st  # For creating web interface
import pandas as pd  # For data manipulation
import datetime as dt  # For date and time manipulation
import os  # For file and directory manipulation

MOOD_FILE = "mood-data.csv"

# Function to load mood data from CSV
def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        return pd.DataFrame(columns=["Time", "Date", "Mood"])  # Return empty DataFrame if file is missing

    try:
        # Read CSV with correct delimiter and ignore bad lines
        df = pd.read_csv(MOOD_FILE, delimiter=",", on_bad_lines="skip")

        # Ensure correct headers
        if not all(col in df.columns for col in ["Time", "Date", "Mood"]):
            return pd.DataFrame(columns=["Time", "Date", "Mood"])  # Reset if headers are incorrect

        return df
    except pd.errors.EmptyDataError:
        st.error("The CSV file is empty or corrupted.")
        return pd.DataFrame(columns=["Time", "Date", "Mood"])  # Handle empty file case

# Function to save mood data to CSV
def save_mood_data(time, date, mood):
    file_exists = os.path.exists(MOOD_FILE) and os.stat(MOOD_FILE).st_size > 0

    try:
        df = pd.DataFrame([[time, date, mood]], columns=["Time", "Date", "Mood"])
        df.to_csv(MOOD_FILE, header=not file_exists, index=False, mode="a", encoding="utf-8", sep=",")
    except Exception as e:
        st.error(f"Error saving data: {e}")

# Streamlit App
st.title("Mood Tracker 😊")

today = dt.date.today()
time = dt.datetime.now().strftime("%H:%M:%S")  # Format time as HH:MM:SS

st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Neutral", "Sad", "Angry"])

if st.button("Log Mood"):
    save_mood_data(time, today, mood)
    st.success("Mood logged successfully! ✅")

# Load and display past mood data
data = load_mood_data()

if not data.empty:
    st.subheader("Mood Trends Over Time 📊")

    try:
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")  # Handle parsing errors safely
        mood_count = data.groupby("Mood")["Date"].count()
        st.bar_chart(mood_count)
    except Exception as e:
        st.error(f"Error processing data: {e}")
