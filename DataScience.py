import altair as alt
import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st

# ---- Page Config ----
st.set_page_config(
    page_title="A/B Testing Dashboard",
    page_icon="🔬",
    layout="wide"
)

# ---- Sidebar with Dark Mode Toggle ----
st.sidebar.title("🔬 A/B Testing Toolkit")
st.sidebar.write("Analyze A/B test results with statistical insights.")

dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode")

# ---- Custom Styling for Dark & Light Modes ----
if dark_mode:
    dark_theme = """
        <style>
            body {
                background-color: #121212;
                color: #ffffff;
            }
            .stApp {
                background-color: #121212;
            }
            .title, .subtitle {
                color: #1db954;
            }
            .stButton>button {
                background-color: #1db954;
                color: white;
                border-radius: 8px;
            }
            .stMetric {
                text-align: center;
                color: #1db954;
            }
        </style>
    """
else:
    dark_theme = """
        <style>
            .title { 
                font-size: 32px; 
                font-weight: bold; 
                color: #4A90E2;
            }
            .subtitle {
                font-size: 24px;
                font-weight: bold;
                color: #0A9396;
                text-align: center;
            }
            .stMetric {
                text-align: center;
            }
        </style>
    """

st.markdown(dark_theme, unsafe_allow_html=True)

# ---- Sample Size Calculation Function ----
def calculate_sample_size(baseline_rate, mde, alpha, power, measurement_type='relative'):
    if measurement_type == 'relative':
        p1 = baseline_rate
        p2 = baseline_rate * (1 + mde)
    else:
        p1 = baseline_rate
        p2 = baseline_rate + mde

    p_pooled = (p1 + p2) / 2
    se = np.sqrt(2 * p_pooled * (1 - p_pooled))
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(power)

    n = ((z_alpha + z_beta) / ((p1 - p2) / se))**2
    return int(np.ceil(n))

# ---- Results Analysis Function ----
def analyze_results(conversions_a, samples_a, conversions_b, samples_b, confidence_level):
    rate_a = conversions_a / samples_a
    rate_b = conversions_b / samples_b
    se_a = np.sqrt(rate_a * (1 - rate_a) / samples_a)
    se_b = np.sqrt(rate_b * (1 - rate_b) / samples_b)
    
    z = (rate_b - rate_a) / np.sqrt(se_a**2 + se_b**2)
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))

    ci_a_lower, ci_a_upper = stats.norm.interval(confidence_level, loc=rate_a, scale=se_a)
    ci_b_lower, ci_b_upper = stats.norm.interval(confidence_level, loc=rate_b, scale=se_b)

    return rate_a, rate_b, p_value, ci_a_lower, ci_a_upper, ci_b_lower, ci_b_upper

# ---- Sidebar Menu ----
st.sidebar.subheader("Navigation")
tab_choice = st.sidebar.radio("Choose a Tool", ["📏 Sample Size Calculator", "📊 Results Analyzer"])

# ---- Sample Size Calculator ----
if tab_choice == "📏 Sample Size Calculator":
    st.markdown("<p class='title'>📏 Sample Size Calculator</p>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        baseline_rate = st.slider("Baseline Conversion Rate (%)", 1, 50, 10, 1) / 100
        mde = st.slider("Minimum Detectable Effect (%)", 1, 50, 5, 1) / 100

    with col2:
        alpha = st.slider("Significance Level (Alpha)", 0.01, 0.1, 0.05, 0.01)
        power = st.slider("Statistical Power", 0.7, 0.99, 0.8, 0.01)

    sample_size = calculate_sample_size(baseline_rate, mde, alpha, power)
    st.success(f"🎯 Required Sample Size per Group: **{sample_size}**")

# ---- A/B Test Results Analyzer ----
elif tab_choice == "📊 Results Analyzer":
    st.markdown("<p class='title'>📊 A/B Test Results Analyzer</p>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        conversions_a = st.number_input("Conversions (Group A)", 0, 100000, 100)
        samples_a = st.number_input("Total Samples (Group A)", 1, 100000, 1000)

    with col2:
        conversions_b = st.number_input("Conversions (Group B)", 0, 100000, 120)
        samples_b = st.number_input("Total Samples (Group B)", 1, 100000, 1000)

    confidence_level = st.slider("Confidence Level", 0.8, 0.99, 0.95, 0.01)

    # Analyze results
    conv_rate_a, conv_rate_b, p_value, ci_a_lower, ci_a_upper, ci_b_lower, ci_b_upper = analyze_results(
        conversions_a, samples_a, conversions_b, samples_b, confidence_level)

    st.metric("Conversion Rate (A)", f"{conv_rate_a:.2%}")
    st.metric("Conversion Rate (B)", f"{conv_rate_b:.2%}")
    
    if p_value < 1 - confidence_level:
        st.success(f"✅ Statistical Significance Achieved! (p = {p_value:.3f})")
    else:
        st.warning(f"⚠️ No Statistical Significance Found (p = {p_value:.3f})")

    # Confidence Interval Table
    results_df = pd.DataFrame({
        "Metric": ["Conversion Rate (A)", "Conversion Rate (B)"],
        "Value": [f"{conv_rate_a:.2%}", f"{conv_rate_b:.2%}"],
        "Confidence Interval": [f"[{ci_a_lower:.2%}, {ci_a_upper:.2%}]", f"[{ci_b_lower:.2%}, {ci_b_upper:.2%}]"]
    })

    st.dataframe(results_df, use_container_width=True)

# ---- Footer ----
st.sidebar.markdown("---")
st.sidebar.markdown("🚀 Built with ❤️ using **Streamlit**")
