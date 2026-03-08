appointments = []

def book_appointment(patient, doctor, date, time):

    for appt in appointments:
        if appt["doctor"] == doctor and appt["date"] == date and appt["time"] == time:
            return {
                "status": "failed",
                "message": "Slot already booked"
            }

    appointment = {
        "patient": patient,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)

    return {
        "status": "success",
        "appointment": appointment
    }


def cancel_appointment(patient, doctor, date, time):

    for appt in appointments:
        if (
            appt["patient"] == patient and
            appt["doctor"] == doctor and
            appt["date"] == date and
            appt["time"] == time
        ):
            appointments.remove(appt)

            return {
                "status": "success",
                "message": "Appointment cancelled"
            }

    return {
        "status": "failed",
        "message": "Appointment not found"
    }


def reschedule_appointment(patient, doctor, old_time, new_time, date):

    for appt in appointments:

        if (
            appt["patient"] == patient and
            appt["doctor"] == doctor and
            appt["time"] == old_time and
            appt["date"] == date
        ):

            for a in appointments:
                if a["doctor"] == doctor and a["date"] == date and a["time"] == new_time:
                    return {
                        "status": "failed",
                        "message": "New slot unavailable"
                    }

            appt["time"] = new_time

            return {
                "status": "success",
                "message": "Appointment rescheduled",
                "appointment": appt
            }

    return {
        "status": "failed",
        "message": "Original appointment not found"
    }