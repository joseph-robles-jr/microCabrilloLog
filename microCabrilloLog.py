import datetime
from datetime import timezone #used for conversion to UTC

def convert_to_utc():
    """Converts a given time to UTC and returns it"""

    #
    dt = datetime.datetime.now(timezone.utc)
    print(dt)


convert_to_utc()
