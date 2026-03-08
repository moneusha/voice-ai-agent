from fastapi import FastAPI
from agent.voice_agent import detect_intent
from scheduler.appointment_service import (
    book_appointment,
    cancel_appointment,
    reschedule_appointment
)
from services.language_detection import detect_language

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Voice AI Agent Running"}


@app.post("/process")
def process_text(text: str):

    intent = detect_intent(text)
    language = detect_language(text)

    return {
        "intent": intent,
        "language": language
    }


@app.post("/book")
def book(patient: str, doctor: str, date: str, time: str):

    result = book_appointment(patient, doctor, date, time)

    return result


@app.post("/cancel")
def cancel(patient: str, doctor: str, date: str, time: str):

    result = cancel_appointment(patient, doctor, date, time)

    return result


@app.post("/reschedule")
def reschedule(patient: str, doctor: str, date: str, old_time: str, new_time: str):

    result = reschedule_appointment(patient, doctor, old_time, new_time, date)

    return result