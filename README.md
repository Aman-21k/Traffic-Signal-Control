# 🚦 Traffic Signal Control using Reinforcement Learning

This project implements a **Reinforcement Learning (Q-Learning)** based system to dynamically control traffic signals at an intersection.  
The goal is to **minimize traffic congestion** by adjusting green signal duration based on real-time traffic conditions.

---

## 📌 Problem Statement
Traditional traffic signals operate on fixed timers, which often leads to:
- Traffic congestion
- Increased waiting time
- Inefficient signal usage

This project solves the problem by using **Reinforcement Learning**, where an agent learns optimal signal control strategies through interaction with the environment.

---

## 🧠 Reinforcement Learning Overview

| RL Component | Description |
|-------------|------------|
| Agent | Traffic Signal Controller |
| Environment | Road Intersection |
| State | Number of vehicles on Road A and Road B |
| Actions | Short, Medium, Long green signal |
| Reward | Negative of total waiting vehicles |
| Algorithm | Q-Learning |

---

## ⚙️ Algorithm Used: Q-Learning

The Q-value update equation:

\[
Q(s,a) = Q(s,a) + \alpha [r + \gamma \max Q(s',a') - Q(s,a)]
\]

Where:
- α → Learning Rate  
- γ → Discount Factor  
- r → Reward
- 

