import streamlit as st
import pandas as pd

st.title("🔍 Track Complaint")

complaint_id = st.text_input(
    "Enter Complaint ID"
)

if st.button("Track"):

    try:

        df = pd.read_csv(
            "data/complaints.csv"
        )

        result = df[
            df["complaint_id"] == complaint_id
        ]

        if not result.empty:

            st.success("Complaint Found")

            st.write(
                "Patient:",
                result.iloc[0]["patient_name"]
            )

            st.write(
                "Category:",
                result.iloc[0]["category"]
            )

            st.write(
                "Status:",
                result.iloc[0]["status"]
            )

            st.write(
                "Priority:",
                result.iloc[0]["priority"]
            )

            st.write(
                "Sentiment:",
                result.iloc[0]["sentiment"]
            )

        else:
            st.error("Complaint Not Found")

    except:
        st.error("No complaints available")