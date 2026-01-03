import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sigmoid Activation", layout="centered")
st.title("Sigmoid Activation Function")

st.write("Sigmoid(x) = 1 / (1 + e^(-x))")

x_min, x_max = st.slider("x range", -20, 20, (-10, 10))
x = np.linspace(x_min, x_max, 500)
y = 1 / (1 + np.exp(-x))

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("Sigmoid(x)")
ax.set_title("Sigmoid Curve")
st.pyplot(fig)

st.markdown("**Note:** outputs between 0 and 1 (often used for probability).")