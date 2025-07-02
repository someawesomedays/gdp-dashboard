import streamlit as st
from datetime import datetime

# Profile details
name = "Jacob Mundell"
birthdate = datetime(1972, 1, 7)
weight_lbs = 187
zodiac = "Capricorn ♑"

# Calculate age
today = datetime.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Streamlit app layout
st.set_page_config(page_title="Jacob's Profile", page_icon="🧠", layout="centered")

st.title("👤 Jacob Mundell's Profile")
st.markdown("---")
st.subheader("📅 Birthday:")
st.write(f"{birthdate.strftime('%B %d, %Y')} ({zodiac})")
st.subheader("🎂 Age:")
st.write(f"{age} years old")
st.subheader("⚖️ Weight:")
st.write(f"{weight_lbs} lbs")
st.subheader("🧠 Personality:")
st.write("Curious, strategic, introspective, Capricorn energy.")
st.markdown("---")
st.info("This is a personal profile app powered by Streamlit.")
