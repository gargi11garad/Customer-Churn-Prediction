import streamlit as st
import pickle
import numpy as np
import pandas as pd
import time

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================

model = pickle.load(open("churn_model.pkl", "rb"))

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

body {
    background-color: #f5f7fa;
}

.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #4A90E2;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.metric-card {
    background: linear-gradient(to right, #4facfe, #00f2fe);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #4facfe, #00f2fe);
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(to right, #43e97b, #38f9d7);
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.markdown('<div class="title">📊 Customer Churn Prediction</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Predict whether a customer will leave the company or stay.</div>',
    unsafe_allow_html=True
)

# =========================
# SIDEBAR INPUTS
# =========================

st.sidebar.header("📌 Enter Customer Details")

tenure = st.sidebar.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

monthlycharges = st.sidebar.slider(
    "Monthly Charges",
    0.0,
    200.0,
    70.0
)

totalcharges = st.sidebar.slider(
    "Total Charges",
    0.0,
    10000.0,
    2000.0
)

contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

payment = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]
)

# =========================
# MAIN LAYOUT
# =========================

col1, col2 = st.columns(2)

# =========================
# CUSTOMER INFO CARD
# =========================

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("👤 Customer Information")

    st.write(f"📅 Tenure: **{tenure} months**")
    st.write(f"💰 Monthly Charges: **₹{monthlycharges}**")
    st.write(f"💳 Total Charges: **₹{totalcharges}**")
    st.write(f"📄 Contract Type: **{contract}**")
    st.write(f"🌐 Internet Service: **{internet}**")
    st.write(f"💵 Payment Method: **{payment}**")

    st.markdown('</div>', unsafe_allow_html=True)

    # Chart
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📈 Customer Charges")

    chart_data = pd.DataFrame({
        "Charges": [monthlycharges, totalcharges]
    }, index=["Monthly", "Total"])

    st.bar_chart(chart_data)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# PREDICTION CARD
# =========================

with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🤖 AI Prediction")

    st.write("Click the button below to predict customer churn.")

    if st.button("🚀 Predict Churn"):

        with st.spinner("Analyzing customer data..."):
            time.sleep(2)

            # IMPORTANT:
            # Replace this with your ACTUAL feature order

            data = np.array([[0,0,tenure,0,0,0,0,0,0,
                              monthlycharges,totalcharges,
                              0,0,0,0,0,0,0,0,0]])

            prediction = model.predict(data)

            st.progress(100)

            if prediction[0] == 1:

                st.error("⚠️ Customer is likely to CHURN")

                st.markdown("""
                ### 🔍 Recommendation
                - Offer discount plans
                - Improve customer support
                - Provide loyalty benefits
                """)

            else:

                st.success("✅ Customer is likely to STAY")

                st.markdown("""
                ### 🎉 Great!
                Customer satisfaction appears good.
                """)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# METRICS SECTION
# =========================

st.markdown("## 📊 Model Performance")

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(
        '<div class="metric-card">Accuracy<br>82%</div>',
        unsafe_allow_html=True
    )

with m2:
    st.markdown(
        '<div class="metric-card">Model<br>Logistic Regression</div>',
        unsafe_allow_html=True
    )

with m3:
    st.markdown(
        '<div class="metric-card">Dataset<br>Telco Customer Churn</div>',
        unsafe_allow_html=True
    )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.markdown(
    """
    <center>
    Made with ❤️ using Streamlit and Machine Learning
    </center>
    """,
    unsafe_allow_html=True
)