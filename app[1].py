import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Inter-Vehicle Distance Gauge", layout="wide")
st.title("IoT-Based Inter-Vehicle Distance Gauge")
st.caption("Arduino Uno + HC-SR04 ultrasonic sensor + buzzer monitoring dashboard")

threshold = st.sidebar.slider("Unsafe distance threshold (cm)", 5, 100, 10)
data = pd.read_csv("data.csv")

distance = st.number_input("Current distance reading (cm)", min_value=0.0, value=float(data["distance_cm"].iloc[-1]))
status = "UNSAFE - BUZZER ON" if distance < threshold else "SAFE - BUZZER OFF"

c1, c2 = st.columns(2)
c1.metric("Distance", f"{distance:.2f} cm")
c2.metric("Status", status)

st.subheader("Recorded Sensor Readings")
fig, ax = plt.subplots()
ax.plot(data["timestamp"], data["distance_cm"], marker="o", markersize=3)
ax.axhline(threshold, linestyle="--", label="Unsafe threshold")
ax.set_xlabel("Timestamp")
ax.set_ylabel("Distance (cm)")
ax.tick_params(axis="x", rotation=45)
ax.legend()
st.pyplot(fig)

st.dataframe(data.tail(20), use_container_width=True)
