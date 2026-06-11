import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Smart Hospital Complaint System", layout="centered")

st.title("🏥 Smart Hospital Complaint System")

menu = ["Raise Complaint", "View Complaints"]
choice = st.sidebar.selectbox("Menu", menu)

if "data" not in st.session_state:
    st.session_state.data = []

if choice == "Raise Complaint":
    st.subheader("📢 Submit Complaint")

    name = st.text_input("Name")
    dept = st.selectbox("Department", ["Hostel", "Classroom", "Lab", "Maintenance"])
    complaint = st.text_area("Complaint")

    if st.button("Submit"):
        if name and complaint:
            st.session_state.data.append({
                "Name": name,
                "Department": dept,
                "Complaint": complaint,
                "Time": str(datetime.datetime.now())
            })
            st.success("Submitted successfully!")
        else:
            st.error("Fill all fields")

elif choice == "View Complaints":
    st.subheader("📋 Complaints List")

    if len(st.session_state.data) == 0:
        st.info("No complaints yet")
    else:
        st.dataframe(pd.DataFrame(st.session_state.data))