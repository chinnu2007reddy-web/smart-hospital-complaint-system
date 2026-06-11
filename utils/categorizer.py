def categorize(text):

    text = text.lower()

    if "doctor" in text:
        return "Doctor Complaint"

    elif "staff" in text:
        return "Staff Behavior"

    elif "appointment" in text:
        return "Appointment Issue"

    elif "medicine" in text:
        return "Medicine Availability"

    elif "bill" in text:
        return "Billing Issue"

    elif "clean" in text:
        return "Cleanliness Issue"

    elif "emergency" in text:
        return "Emergency Service Issue"

    else:
        return "General Complaint"