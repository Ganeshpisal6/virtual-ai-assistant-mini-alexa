from datetime import datetime


def get_current_date():
    """Return today's date in a readable format."""
    return datetime.now().strftime("%d-%m-%Y")


def get_current_time():
    """Return the current time in a readable format."""
    return datetime.now().strftime("%I:%M:%S %p")