import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/NewYork",
    "Europe/London",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Asia/Tokyo",
    "Asia/Dubai",
    "Asia/Kolkata",
    "Europe/Paris",
    "Europe/Berlin",
    "Asia/Shanghai",
    "America/Chicago",
    "America/Toronto",
    "Turkey/Eastern",
    "Turkey/Central",
    "Turkey/Pacific",
    "Turkey/Mountain",
    "Israel/Tel_Aviv",
    "Australia/Melbourne",
    "Indonesia/Jakarta",
    "Russia/Moscow",
]

st.title("Time Zone Converter")

selected_time_zone = st.multiselect("Select Time Zones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.subheader("Selected TimeZone")

for tz in selected_time_zone:
    try:
        current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d  %I  %H:%M:%S %p")
        st.write(f"**{tz}** : {current_time}")
    except Exception as e:
        st.error(f"Error fetching time for {tz}: {e}")

st.subheader("Convert Time Between Time Zones")

try:
    current_time = st.time_input("Select Time", value=datetime.now().time())
    from_tz = st.selectbox("From Time Zone", TIME_ZONES, index=0)
    to_tz = st.selectbox("To Time Zone", TIME_ZONES, index=1)

    if st.button("Convert Time"):
        try:
            dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
            converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d  %I   %H:%M:%S %p")
            st.success(f"Converted Time in {to_tz} : {converted_time}")
        except Exception as e:
            st.error(f"Error converting time: {e}")
except Exception as e:
    st.error(f"Error in time selection: {e}")


st.write("Developed by: [Muhammad Emad Hassan](hhttps://www.linkedin.com/in/muhammad-emad-hassan)")