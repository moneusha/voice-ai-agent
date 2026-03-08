appointments = []

def create_appointment(patient, doctor, date, time):
    appointment = {
        "patient": patient,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)
    return appointment


def get_appointments():
    return appointments