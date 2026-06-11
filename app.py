import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Smart Hospital Complaint System",
    page_icon="🏥",
    layout="wide"
)

# Logo (Optional)
try:
    st.image(
        "assets/hospital_logo.png",
        width=120
    )
except:
    pass

# Title
st.title("🏥 Smart Hospital Complaint System")

st.markdown("""
### AI-Powered Hospital Complaint Management

This platform helps patients report and track complaints efficiently.

### Features

✅ Submit Complaints

✅ Track Complaint Status

✅ Dashboard Analytics

✅ Admin Management Panel

✅ Sentiment Analysis

✅ Complaint Categorization

✅ Priority Prediction
""")

# Sidebar
st.sidebar.title("Navigation")

st.sidebar.success(
    "Select a page from the sidebar."
)

# Home Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📋 Complaint Reporting")

with col2:
    st.success("🤖 AI Classification")

with col3:
    st.warning("📊 Analytics Dashboard")

st.divider()

# About Project
st.subheader("About Project")

st.write("""
The Smart Hospital Complaint System is designed to improve patient satisfaction by providing an easy way to report issues related to:

- Doctor Complaints
- Staff Behavior
- Appointment Delays
- Medicine Availability
- Billing Problems
- Hospital Cleanliness

The system uses simple AI techniques to automatically:

- Detect complaint sentiment
- Categorize complaints
- Assign priority levels
""")

st.divider()

# Quick Guide
st.subheader("How to Use")

st.markdown("""
### Patient

1. Open **Submit Complaint**
2. Enter your complaint details
3. Submit complaint
4. Save Complaint ID
5. Track status using Track Complaint page

### Administrator

1. Open Admin Panel
2. Enter Admin Password
3. View complaints
4. Update complaint status
5. Monitor dashboard analytics
""")

st.divider()

# Footer
st.markdown(
    """
    ---
    Developed using **Streamlit + Pandas + TextBlob**
    """
)