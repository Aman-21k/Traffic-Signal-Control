import streamlit as st
import numpy as np
from environment import TrafficEnvironment

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Traffic Signal RL",
    page_icon="🚦",
    layout="centered"
)

# -----------------------------
# Load Q-table
# -----------------------------
q_table = np.load("q_table.npy")

import streamlit as st
import numpy as np
from environment import TrafficEnvironment

st.set_page_config(page_title="Traffic RL", page_icon="🚦")

q_table = np.load("q_table.npy")

# -----------------------------
# ENVIRONMENT IN SESSION STATE
# -----------------------------
if "env" not in st.session_state:
    st.session_state.env = TrafficEnvironment()
    st.session_state.state = st.session_state.env.reset()
    st.session_state.done = False

env = st.session_state.env


# -----------------------------
# Title
# -----------------------------
st.title("🚦 Traffic Signal Control using Reinforcement Learning")
st.markdown("This app simulates an RL-based smart traffic signal.")

st.divider()

# -----------------------------
# Session state
# -----------------------------
if "state" not in st.session_state:
    st.session_state.state = env.reset()
    st.session_state.done = False

# -----------------------------
# Display current state
# -----------------------------
road_A, road_B = st.session_state.state

col1, col2 = st.columns(2)
col1.metric("🚗 Cars on Road A", road_A)
col2.metric("🚙 Cars on Road B", road_B)

# -----------------------------
# Action button
# -----------------------------
a, b = st.session_state.state

if st.button("Next Action"):
    if not st.session_state.done:
        action = np.argmax(q_table[a, b])
        next_state, reward, done = env.step(action)

        st.session_state.state = next_state
        st.session_state.done = done

        st.success(f"Action Taken: {action}")
        st.info(f"Reward: {reward}")


    else:
        st.warning("Traffic already cleared!")

# -----------------------------
# Reset button
# -----------------------------
if st.button("🔄 Reset Simulation"):
    st.session_state.state = env.reset()
    st.session_state.done = False
    st.rerun()



# -----------------------------
# Completion message
# -----------------------------
if st.session_state.done:
    st.balloons()
    st.success("🎉 Traffic Cleared Successfully!")
