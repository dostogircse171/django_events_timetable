from django.utils import timezone
from datetime import datetime, date

def days_to_date(target_date: date) -> int:
    """
    Calculates the number of days from the current date to the target date, considering timezones.

    Args:
        target_date (datetime): A datetime object representing the future or past date.

    Returns:
        int:    The number of days between the current date and the provided target date. 
                Returns a negative number if the provided date is in the past.
    """

    if not isinstance(target_date, date):
        raise ValueError("target_date must be a datetime.date object.")
    
    today = timezone.now()

    delta = target_date - today.date()

    return delta.days