# 🏥 Smart Hospital Complaint System

An AI-powered Hospital Complaint Management System built using Streamlit and Pandas.

## Features

### Patient Features

* Submit complaints
* Upload complaint evidence
* Track complaint status
* View complaint priority

### Admin Features

* View all complaints
* Update complaint status
* Dashboard analytics
* Complaint monitoring

### AI Features

* Sentiment Analysis
* Complaint Categorization
* Priority Prediction

## Project Structure

smart_hospital_complaint_system/

├── app.py

├── pages/

│ ├── submit_complaint.py

│ ├── track_complaint.py

│ ├── dashboard.py

│ └── admin_panel.py

├── data/

│ ├── complaints.csv

│ └── users.csv

├── utils/

│ ├── data_handler.py

│ ├── sentiment.py

│ ├── categorizer.py

│ ├── priority.py

│ └── notifications.py

├── uploads/

├── assets/

│ └── hospital_logo.png

├── requirements.txt

└── README.md

## Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

## Admin Login

Password:

```text
admin123
```

## Technologies Used

* Python
* Streamlit
* Pandas
* Plotly
* TextBlob

## Future Enhancements

* User Authentication
* Email Notifications
* Hospital Chatbot
* PDF Report Generation
* Machine Learning Models
* Cloud Deployment

## Author

Vishal Reddy
