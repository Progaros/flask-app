# nice_module.py

from datetime import datetime

def nice_function():
    now = datetime.now()
    return f"Current time: {now.strftime('%H:%M:%S')}"
