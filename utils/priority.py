def predict_priority(text):

    text = text.lower()

    high_priority_words = [
        "critical",
        "emergency",
        "urgent",
        "serious",
        "danger"
    ]

    medium_priority_words = [
        "delay",
        "appointment",
        "staff",
        "doctor"
    ]

    for word in high_priority_words:

        if word in text:
            return "High"

    for word in medium_priority_words:

        if word in text:
            return "Medium"

    return "Low"