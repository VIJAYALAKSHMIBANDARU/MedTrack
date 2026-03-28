import pandas as pd

def explore():

    patients = pd.read_csv("data/Patients.csv")
    appointments = pd.read_csv("data/Appointments.csv")

    print("Patients shape:", patients.shape)
    print("Appointments shape:", appointments.shape)

    print("\nPatients columns:")
    print(patients.columns)

    print("\nAppointments columns:")
    print(appointments.columns)

    print("\nMissing values:")
    print(patients.isnull().sum())

if __name__ == "__main__":
    explore()
