import streamlit as st
import pandas as pdp

# Set page configuration
st.set_page_config(
    page_title="Customer Churn Hinter",
    page_icon="👋",
    layout="wide",  # Use wide layout for more space
    initial_sidebar_state="expanded",  # Sidebar expanded by default
)

# Custom CSS to beautify the page
st.markdown("""
    <style>
    .main {
        background: #f5f5f5;
    }
    .stApp {
        background-image: url('https://your-background-image-url.com');
        background-size: cover;
    }
    .title {
        color: #4CAF50;
        font-size: 2.5em;
        text-align: center;
        margin-bottom: 20px;
    }
    .welcome {
        color: #555;
        font-size: 1.2em;
        text-align: center;
    }
    .description {
        color: #777;
        font-size: 1.1em;
        text-align: justify;
        margin: 20px;
    }
    .feature-section {
        margin: 20px 0;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("<div class='title'>CUSTOMER CHURN PREDICTION</div>", unsafe_allow_html=True)
st.markdown("<div class='welcome'>Welcome to the Customer Churn prediction app! 👋</div>", unsafe_allow_html=True)
st.markdown("""
<div class='description'>
    This application uses machine learning to predict customer churn. 
    Understanding why customers leave can help you improve retention strategies and grow your business.
</div>
""", unsafe_allow_html=True)

# Adding some sections to describe the app and its features
st.markdown("""
<div class='feature-section'>
    <h2>Features</h2>
    <ul>
        <li>Upload customer data</li>
        <li>Visualize important trends and patterns</li>
        <li>Predict customer churn with advanced ML models</li>
        <li>Interactive dashboards and reports</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Adding interactive widgets
st.sidebar.header("Navigation")
st.sidebar.write("Use the sidebar to navigate through different sections of the app.")

st.sidebar.subheader("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(data.head())

st.sidebar.subheader("Settings")
model_selection = st.sidebar.selectbox("Choose Model", ["Logistic Regression", "Random Forest", "XGBoost"])

st.sidebar.subheader("About")
st.sidebar.write("This app is developed to help businesses understand and predict customer churn using machine learning.")

# Call to action button
if st.button("Get Started"):
    st.write("Let's get started with predicting customer churn!")



