def detect_intent(text):
    
    text = text.lower()

    if "book" in text:
        return "book"

    if "cancel" in text:
        return "cancel"

    if "reschedule" in text:
        return "reschedule"

    return "unknown"