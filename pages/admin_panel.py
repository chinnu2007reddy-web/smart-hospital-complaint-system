import streamlit as st
import pandas as pd

st.title("🛠 Admin Panel")

password = st.text_input(
    "Admin Password",
    type="password"
)

if password == "admin123":

    try:

        df = pd.read_csv(
            "data/complaints.csv"
        )

        st.dataframe(df)

        st.subheader(
            "Update Complaint Status"
        )

        complaint_id = st.selectbox(
            "Complaint ID",
            df["complaint_id"]
        )

        status = st.selectbox(
            "Status",
            [
                "Pending",
                "Under Review",
                "Resolved"
            ]
        )

        if st.button("Update"):

            df.loc[
                df["complaint_id"] == complaint_id,
                "status"
            ] = status

            df.to_csv(
                "data/complaints.csv",
                index=False
            )

            st.success(
                "Status Updated Successfully"
            )

    except:
        st.warning(
            "No complaint records available."
        )

elif password != "":
    st.error(
        "Invalid Admin Password"
    )