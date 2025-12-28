# r2k-qai
Transforming QA with AI: My Open-Source Test Scenario Generator

# AI Test Scenario Generator

An open-source, AI-powered test scenario generator for QA teams. It converts user requirements into risk-based, categorized test scenarios with AI-driven recommendations.

<img width="1920" height="883" alt="image" src="https://github.com/user-attachments/assets/6f5bbe00-0fd3-40c2-9b2b-d579853dca0e" />


## Features
- Risk-based test strategy
- Automation vs manual test categorization
- Edge case identification
- Performance testing profile with Iperf examples
- SaaS-specific checks
- Accessibility checklist
- Cross-browser/device testing
- Security test matrix (OWASP Top 5)
- Disclaimer: Requires QA expert review

## Demo Use Case
Push daily ERP sales data to a data warehouse and pull summarized reports via a dashboard.

## How to Run
Download python code app.py & Run the file from your local - Make sure use your API key
This code is used model": "mistralai/mistral-7b-instruct:free"
cd ai-test-scenario-generator
run : streamlit run R2K_QAI.py --server.port 8501

