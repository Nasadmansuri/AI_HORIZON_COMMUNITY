import streamlit as st

# -------------------------------
# App Config
# -------------------------------
st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
st.markdown("Perform arithmetic operations interactively.")

# -------------------------------
# Input Fields
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First Number", value=0.0, format="%f", key="num1")

with col2:
    num2 = st.number_input("Second Number", value=0.0, format="%f", key="num2")

# -------------------------------
# Operation Dropdown
# -------------------------------
operation = st.selectbox(
    "Select Operation",
    options=["➕ Addition", "➖ Subtraction", "✖️ Multiplication", "➗ Division",
             "% Modulus", "** Power"],
)

# -------------------------------
# Compute Result
# -------------------------------
def calculate(a, b, op):
    if op == "➕ Addition":
        return a + b, f"{a} + {b}"
    elif op == "➖ Subtraction":
        return a - b, f"{a} - {b}"
    elif op == "✖️ Multiplication":
        return a * b, f"{a} × {b}"
    elif op == "➗ Division":
        if b == 0:
            return None, f"{a} ÷ {b}"
        return a / b, f"{a} ÷ {b}"
    elif op == "% Modulus":
        if b == 0:
            return None, f"{a} % {b}"
        return a % b, f"{a} % {b}"
    elif op == "** Power":
        return a ** b, f"{a} ^ {b}"

# -------------------------------
# Calculate Button
# -------------------------------
if st.button("Calculate", use_container_width=True, type="primary"):
    result, expression = calculate(num1, num2, operation)

    st.divider()

    if result is None:
        st.error("❌ Error: Division by zero is not allowed.")
    else:
        # Format result: show int if whole number, else float
        result_display = int(result) if isinstance(result, float) and result.is_integer() else round(result, 10)

        st.markdown("#### Result")
        st.success(f"**{expression} = {result_display}**")

        # Extra detail
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Input A", num1)
        col_b.metric("Input B", num2)
        col_c.metric("Output", result_display)

    # -------------------------------
    # History (session state)
    # -------------------------------
    if "history" not in st.session_state:
        st.session_state.history = []

    entry = f"{expression} = {result if result is not None else 'Error'}"
    if entry not in st.session_state.history:
        st.session_state.history.insert(0, entry)

# -------------------------------
# Calculation History
# -------------------------------
if "history" in st.session_state and st.session_state.history:
    st.divider()
    st.markdown("#### 🕘 Calculation History")

    for i, item in enumerate(st.session_state.history[:10]):
        st.text(f"{i + 1}.  {item}")

    if st.button("🗑️ Clear History", use_container_width=True):
        st.session_state.history = []
        st.rerun()
        