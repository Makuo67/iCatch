import time


def real_time_text_generator(text):
    for char in text:
        time.sleep(0.05)  # Simulate delay for real-time streaming
        yield char
