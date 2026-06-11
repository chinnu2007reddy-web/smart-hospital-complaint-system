import pandas as pd
import os

COMPLAINT_FILE = "data/complaints.csv"


def load_complaints():
    if os.path.exists(COMPLAINT_FILE):
        return pd.read_csv(COMPLAINT_FILE)

    columns = [
        "complaint_id",
        "patient_name",
        "category",
        "description",
        "sentiment",
        "priority",
        "status",
        "date",
        "image"
    ]

    return pd.DataFrame(columns=columns)


def save_complaint(data):

    df = load_complaints()

    new_row = pd.DataFrame([data])

    df = pd.concat(
        [df, new_row],
        ignore_index=True
    )

    df.to_csv(
        COMPLAINT_FILE,
        index=False
    )


def get_complaint(complaint_id):

    df = load_complaints()

    result = df[
        df["complaint_id"] == complaint_id
    ]

    return result


def update_status(
    complaint_id,
    new_status
):

    df = load_complaints()

    df.loc[
        df["complaint_id"] == complaint_id,
        "status"
    ] = new_status

    df.to_csv(
        COMPLAINT_FILE,
        index=False
    )