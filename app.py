%%writefile app.py
import streamlit as st

# 🎨 Streamlit App Title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator")
st.write("A basic calculator built with **Streamlit** in Python.")

# 📥 Input fields
num1 = st.number_input("Enter first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter second number:", value=0.0, step=1.0)

# ➕ Choose operation
operation = st.selectbox(
    "Choose operation:",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# 🧠 Perform calculation
result = None
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (×)":
            result = num1 * num2
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("🚫 Cannot divide by zero!")
            else:
                result = num1 / num2

        if result is not None:
            st.success(f"✅ Result: **{result}**")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
