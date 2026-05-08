import streamlit as st
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Churn App", layout="wide")

# -------------------------------
# USER AUTH SYSTEM
# -------------------------------
def load_users():
    if os.path.exists("users.pkl"):
        return pickle.load(open("users.pkl", "rb"))
    return {}

def save_users(users):
    pickle.dump(users, open("users.pkl", "wb"))

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = ""

if "page" not in st.session_state:
    st.session_state.page = "Home"

users = load_users()

# -------------------------------
# LOGIN PAGE
# -------------------------------
if not st.session_state.logged_in:

    st.markdown("<h1 style='text-align:center;'>🔐 Login System</h1>", unsafe_allow_html=True)

    option = st.radio("Select", ["Login", "Register"])

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if option == "Register":
        if st.button("Register"):
            if email in users:
                st.error("User already exists")
            else:
                users[email] = password
                save_users(users)
                st.success("Registered! Now login.")

    if option == "Login":
        if st.button("Login"):
            if email in users and users[email] == password:
                st.session_state.logged_in = True
                st.session_state.user = email
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.stop()

# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------
st.sidebar.title("📊 Dashboard")
st.sidebar.write(f"👋 {st.session_state.user}")

page = st.sidebar.radio("Navigate", ["Home", "Prediction", "Insights", "About"])

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

# -------------------------------
# LOAD MODEL + DATA
# -------------------------------
model = pickle.load(open("churn_model.pkl", "rb"))
df = pd.read_csv("custome.csv")

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "Home":

    st.title("📊 Customer Churn Prediction")

    col1, col2 = st.columns([2,1])

    with col1:
        st.subheader("🚀 Overview")
        st.write("""
        ✔ Predict customer churn  
        ✔ Analyze business insights  
        ✔ Improve retention  
        """)

        st.subheader("📌 How to Use")
        st.write("""
        - Go to Prediction  
        - Enter customer details  
        - Check churn risk  
        """)

    with col2:
        st.metric("Accuracy", "83%")
        st.metric("Recall", "86%")
        st.metric("Dataset", "20K+")

# -------------------------------
# PREDICTION PAGE
# -------------------------------
elif page == "Prediction":

    st.title("🔍 Predict Customer Churn")

    col1, col2 = st.columns(2)

    with col1:
        tenure = st.number_input("Tenure", 0, 100)
        monthly_charges = st.number_input("Monthly Charges", 0.0, 10000.0)
        total_charges = st.number_input("Total Charges", 0.0, 100000.0)

    with col2:
        support_calls = st.number_input("Support Calls", 0, 50)
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        payment_method = st.selectbox("Payment Method", ["Credit card", "Bank transfer", "Electronic check"])
        tech_support = st.selectbox("Tech Support", ["Yes", "No"])
        online_security = st.selectbox("Online Security", ["Yes", "No"])
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    if st.button("Predict"):

        input_df = pd.DataFrame([{
            'tenure': tenure,
            'monthly_charges': monthly_charges,
            'total_charges': total_charges,
            'support_calls': support_calls,
            'contract': contract,
            'payment_method': payment_method,
            'tech_support': tech_support,
            'online_security': online_security,
            'internet_service': internet_service
        }])

        prob = model.predict_proba(input_df)[0][1]
        pred = model.predict(input_df)[0]

        st.metric("Churn Probability", f"{prob*100:.2f}%")

        if prob > 0.7:
            st.error("🟥 HIGH RISK")
        elif prob > 0.4:
            st.warning("🟨 MEDIUM RISK")
        else:
            st.success("🟩 LOW RISK")

        if pred == 1:
            st.error("Customer will churn")
        else:
            st.success("Customer will stay")

# -------------------------------
# INSIGHTS PAGE
# -------------------------------
elif page == "Insights":

    st.title("📊 Insights Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots()
        sns.countplot(x='churn', data=df, ax=ax)
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        df['churn'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        st.pyplot(fig)

    st.subheader("Contract vs Churn")
    fig, ax = plt.subplots()
    sns.countplot(x='contract', hue='churn', data=df, ax=ax)
    st.pyplot(fig)

    st.subheader("Tenure vs Churn")
    fig, ax = plt.subplots()
    sns.boxplot(x='churn', y='tenure', data=df, ax=ax)
    st.pyplot(fig)

    st.success("""
    ✔ Month-to-month users churn more  
    ✔ New customers churn more  
    ✔ High support calls increase churn  
    """)

# -------------------------------
# ABOUT PAGE
# -------------------------------
elif page == "About":

    st.title("📁 About")

    st.write("""
    This project predicts customer churn using Machine Learning.

    Models Used:
    - Logistic Regression
    - Random Forest

    Accuracy: 83%  
    Recall: 86%
    """)