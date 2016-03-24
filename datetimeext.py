import re
from datetime import datetime, timedelta, timezone


def to_timestamp(dt_str, tz_str):

    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    str_delta = re.match(r'^UTC([+|-]+)(\d{1,2}):(\d{2})$', tz_str)

    if str_delta:
        delta = int(str_delta.group(1) + str_delta.group(2))
        tz = timezone(timedelta(hours=delta))
        result_dt = cday.replace(tzinfo=tz)
        return result_dt.timestamp()
    else:
        return ''


t1 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-6-1 08:10:30', 'UTC+07:00')
assert t2 == 1433121030.0, t2

print('Pass')