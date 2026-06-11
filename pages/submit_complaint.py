import streamlit as st
import pandas as pd
import uuid
from datetime import datetime

from utils.sentiment import analyze_sentiment
from utils.categorizer import categorize
from utils.priority import predict_priority
from utils.data_handler import save_complaint

st.title("🏥 Submit Complaint")

name = st.text_input("Patient Name")

description = st.text_area("Complaint Description")

uploaded_file = st.file_uploader(
    "Upload Evidence (Optional)",
    type=["png", "jpg", "jpeg"]
)

if st.button("Submit Complaint"):

    if name and description:

        complaint_id = str(uuid.uuid4())[:8]

        sentiment = analyze_sentiment(description)

        category = categorize(description)

        priority = predict_priority(description)

        image_name = ""

        if uploaded_file:

            image_name = uploaded_file.name

            with open(
                f"uploads/{image_name}",
                "wb"
            ) as f:
                f.write(uploaded_file.getbuffer())

        data = {
            "complaint_id": complaint_id,
            "patient_name": name,
            "category": category,
            "description": description,
            "sentiment": sentiment,
            "priority": priority,
            "status": "Pending",
            "date": datetime.now(),
            "image": image_name
        }

        save_complaint(data)

        st.success(
            f"Complaint Submitted Successfully!\nComplaint ID: {complaint_id}"
        )

    else:
        st.warning("Please fill all required fields.")