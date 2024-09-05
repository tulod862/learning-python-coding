
from datetime import datetime
from dateutil.relativedelta import relativedelta

def time_until_event(description_str):
    try:
        _, date_str = description_str.split(maxsplit=1)
        today = datetime.now().date()
        event_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        delta = relativedelta(event_date, today)
        total_days_left = (event_date - today).days
        months_left = delta.years * 12 + delta.months
        days_left = delta.days
        
        if event_date < today:
            return f"The event date {event_date} has already passed."
        
        return f"{months_left} months and {days_left} days left until the event."

    except ValueError as e:
        return str(e)


description = "Meeting 2025-06-13"
time_left = time_until_event(description)
print(time_left)