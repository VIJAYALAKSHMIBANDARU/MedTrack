import pandas as pd

def load_and_merge():

    patients = pd.read_csv("data/Patients.csv")
    appointments = pd.read_csv("data/Appointments.csv")

    df = appointments.merge(
        patients,
        on="patient_id",
        how="left"
    )

    return df


def remove_leakage(df):

    leakage_cols = [
        "appointment_status",
        "treatment_completed_flag",
        "reminder_delivery_status",
        "doctor_avg_daily_load",
        "doctor_experience_years",
        "doctor_id",
        "appointment_id"
    ]

    df.drop(
        columns=[c for c in leakage_cols if c in df.columns],
        inplace=True
    )

    return df
