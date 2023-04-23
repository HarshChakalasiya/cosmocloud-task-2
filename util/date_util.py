from datetime import datetime

import pytz


class Timezones(object):
    UTC = pytz.utc


class DateUtil(object):
    def get_current_timestamp(self) -> int:
        return int(datetime.utcnow().replace(tzinfo=Timezones.UTC).timestamp())