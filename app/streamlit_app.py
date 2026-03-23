
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from models.predict import predict_loan

st.set_page_config(
    page_title="Loan Approval Prediction",
    layout="wide",
)

st.markdown(
    """
    <style>
        .main {
            padding: 2rem 3rem;
            background-color: #0f172a;
            color: #e5e7eb;
        }
        .stButton>button {
            background: linear-gradient(90deg, #4f46e5, #6366f1);
            color: white;
            border-radius: 999px;
            padding: 0.6rem 2.5rem;
            border: none;
            font-weight: 600;
        }
        .stButton>button:hover {
            filter: brightness(1.05);
        }
        .info-card {
            padding: 1rem 1.5rem;
            border-radius: 0.75rem;
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(148, 163, 184, 0.35);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Loan Approval Prediction")
st.caption("Enter applicant details to estimate whether a loan is likely to be approved.")
st.markdown("### Applicant details")

with st.form("loan_prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])

    with col2:
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
        credit_history = st.selectbox("Credit History (1 = good, 0 = poor)", [1.0, 0.0])

    st.markdown("### Financial information")

    fin_col1, fin_col2 = st.columns(2)

    with fin_col1:
        applicant_income = st.number_input(
            "Applicant Income",
            min_value=0.0,
            step=1000.0,
            help="Monthly income of the primary applicant.",
        )
        loan_amount = st.number_input(
            "Loan Amount",
            min_value=0.0,
            step=100.0,
            help="Requested loan amount.",
        )

    with fin_col2:
        coapplicant_income = st.number_input(
            "Coapplicant Income",
            min_value=0.0,
            step=1000.0,
            help="Monthly income of the co-applicant (if any).",
        )
        loan_term = st.number_input(
            "Loan Amount Term (in days)",
            min_value=0.0,
            step=12.0,
            help="Loan repayment term.",
        )

    submitted = st.form_submit_button("Predict loan status")

if submitted:
    data = {
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area,
    }

    prediction = predict_loan(data)

    approved = prediction in (1, "Y", "Approved")

    result_col1, result_col2 = st.columns([2, 1])

    with result_col1:
        if approved:
            st.success("Loan is likely to be approved based on the provided details.")
        else:
            st.error("Loan is unlikely to be approved based on the provided details.")

    with result_col2:
        st.markdown(
            """
            <div class="info-card">
                <strong>Note</strong><br/>
                This is an automated estimate from a model and should not be treated as financial advice.
            </div>
            """,
            unsafe_allow_html=True,
        )