import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
st.write("Perform basic math operations easily with this Streamlit app.")

# Input fields
num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

# Operation selection
operation = st.selectbox("Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform calculation
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            st.error("🚫 Cannot divide by zero!")
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"✅ Result: {result}")

