import streamlit as st
import requests
import re

# -------------------------------
# Configurations
# -------------------------------
API_KEY = "Your Own Key"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
# -------------------------------
# Function: Call Mistral API
# -------------------------------
def call_mistral_api(requirements, push_details, pull_details):
    prompt = f"""
You are an experienced QA test architect with 25 years of experience. Analyze the following and generate concise, categorized test scenarios with risk-based strategy and AI-driven recommendations.

User Requirements:
{requirements}

Push System Details:
{push_details}

Pull System Details:
{pull_details}

Output Requirements:
- Risk-Based Test Strategy (description only)
- Smart Scenario Categorization (Automation Candidates/Manual)
- Edge Case Limit: 2
- Performance Testing Profile (if applicable)
- Network performance using Iperf (if applicable)
- Sample Iperf test code (if applicable)
- SaaS-specific tests (if applicable)
- Accessibility Checklist (if applicable)
- Cross-Browser/Device Matrix (if applicable)
- Security Test Matrix (OWASP Top 5 alignment)
- Disclaimer: Requires QA expert review to conclude the scope
Generate only applicable categories. Avoid test steps.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1500,
        "temperature": 0.3
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "No content returned.")
    except requests.exceptions.RequestException as e:
        return f"API Error: {str(e)}"

# -------------------------------
# Function: Clean AI Output
# -------------------------------
def clean_output(text):
    text = re.sub(r'\*\*+', '', text)  # Remove bold formatting
    text = re.sub(r'\n{3,}', '\n\n', text)  # Remove excessive blank lines
    return text.strip()

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="AI Test Scenario Generator", layout="wide")
st.title("AI-Powered Test Scenario Generator-R2K-QAI")
st.markdown(
    "Generate risk-based, categorized QA test scenarios using AI. "
    "Supports automation candidates, performance, security, accessibility, and cross-browser testing."
)

# Sidebar for input
with st.sidebar:
    st.header("Scenario Configuration")
    requirements = st.text_area("User Requirements", height=150)
    push_details = st.text_area("Push System Details (or NA)", height=100)
    pull_details = st.text_area("Pull System Details (or NA)", height=100)
    generate_button = st.button("Generate Test Scenarios")

# -------------------------------
# Generate and display output
# -------------------------------
if generate_button:
    if not all([requirements.strip(), push_details.strip(), pull_details.strip()]):
        st.warning("Please fill all fields to proceed.")
    else:
        with st.spinner("Generating AI-driven test scenarios..."):
            ai_result = call_mistral_api(requirements, push_details, pull_details)
            cleaned_result = clean_output(ai_result)
        st.subheader("Generated Test Scenarios")
        st.markdown(cleaned_result, unsafe_allow_html=True)