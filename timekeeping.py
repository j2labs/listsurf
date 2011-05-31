from time import mktime
from datetime import datetime
from dateutil.parser import parse

from dictshield.fields import LongField


###
### Converstion Helpers
###

def datestring_to_millis(ds):
    """Takes a string representing the date and converts it to milliseconds
    since epoch.
    """
    dt = parse(ds)
    return datetime_to_millis(dt)

def datetime_to_millis(dt):
    """Takes a datetime instances and converts it to milliseconds since epoch.
    """
    seconds = dt.timetuple()
    seconds_from_epoch = mktime(seconds)
    return seconds_from_epoch * 1000 # milliseconds

def millis_to_datetime(ms):
    """Converts milliseconds into it's datetime equivalent
    """
    seconds = ms / 1000.0
    return datetime.fromtimestamp(seconds)

###
### Time Fields
###

class MillisecondField(LongField):
    """High precision time field.
    """
    def __set__(self, instance, value):
        """__set__ is overriden to allow accepting date strings as input.
        dateutil is used to parse strings into milliseconds.
        """
        if isinstance(value, (str, unicode)):
            value = datestring_to_millis(value)
        instance._data[self.field_name] = value


