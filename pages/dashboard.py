import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Complaint Dashboard")

try:

    df = pd.read_csv(
        "data/complaints.csv"
    )

    total = len(df)

    resolved = len(
        df[df["status"] == "Resolved"]
    )

    pending = len(
        df[df["status"] == "Pending"]
    )

    high = len(
        df[df["priority"] == "High"]
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total",
        total
    )

    c2.metric(
        "Resolved",
        resolved
    )

    c3.metric(
        "Pending",
        pending
    )

    c4.metric(
        "High Priority",
        high
    )

    st.subheader("Category Distribution")

    fig1 = px.pie(
        df,
        names="category"
    )

    st.plotly_chart(fig1)

    st.subheader("Priority Distribution")

    fig2 = px.bar(
        df["priority"].value_counts()
    )

    st.plotly_chart(fig2)

except:
    st.warning(
        "No complaint data found."
    )