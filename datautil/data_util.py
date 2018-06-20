
import datetime
import time
import calendar
from datetime import timedelta


class DateUtil():
    # 获取current_day的开始时间，如果current_day不传 则默认为当前天的开始时间
    @staticmethod
    def get_current_start_time(current_day=None):
        if current_day is None:
            current_day = datetime.datetime.now()
        date = datetime.datetime(current_day.year, current_day.month, current_day.day, 0, 0, 0)
        return date

    @staticmethod
    def get_yesterday_start_time():
        current_day = datetime.datetime.now()
        yesterday = DateUtil.add_day(-1, current_day)
        date = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0)
        return date

    @staticmethod
    def get_week_in_year(current_day=None):
        if current_day is None:
            current_day = datetime.datetime.now()
        return current_day.strftime("%W")

    # 获取current_day的结束时间，如果current_day不传 则默认为当前天的结束时间
    @staticmethod
    def get_current_end_time(current_day=None):
        if current_day is None:
            current_day = datetime.datetime.now()
        date = datetime.datetime(current_day.year, current_day.month, current_day.day, 23, 59, 59)
        return date

    @staticmethod
    def get_yesterday_end_time():
        current_day = datetime.datetime.now()
        yesterday = DateUtil.add_day(-1, current_day)
        date = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 23, 59, 59)
        return date

    # 对current_day的相加days天  如果current_day不传 则默认为当前天
    @staticmethod
    def add_day(days, current_day=None):
        if current_day is None:
            current_day = datetime.datetime.now()
        oneday = datetime.timedelta(days=days)
        day = current_day + oneday
        date = datetime.datetime(day.year, day.month, day.day, current_day.hour, current_day.minute, current_day.second)
        return date

    # 对current_day的相加hours时  如果current_day不传 则默认为当前天
    @staticmethod
    def add_hours(hours, current_day=None):
        if current_day is None:
            current_day = datetime.datetime.now()
        oneday = datetime.timedelta(hours=hours)
        day = current_day + oneday
        date = datetime.datetime(day.year, day.month, day.day, day.hour, current_day.minute, current_day.second)
        return date

    # 获取月份的第一天
    @staticmethod
    def get_month_first_day(current_day=None):
        if current_day is None:
            current_day = datetime.datetime.now()
        year = current_day.year
        month = current_day.month
        date = datetime.datetime(year, month, 1, 0, 0, 0)
        return date
        day = calendar.monthrange(year, month)


    # 获取月份的最后一天
    @staticmethod
    def get_month_end_day(current_day=None):
        if current_day is None:
            current_day = datetime.datetime.now()
        year = current_day.year
        month = current_day.month
        day = calendar.monthrange(year, month)
        date = datetime.datetime(year, month, day[1], 0, 0, 0)
        return date

    # 获取自然周第一天
    @staticmethod
    def get_week_first_day(current_day=None):
        if current_day is None:
            current_day = datetime.datetime.now()

        date = current_day - datetime.timedelta(days=current_day.weekday())
        return datetime.datetime(date.year, date.month, date.day, 0, 0, 0)

    # 获取自然周第最后一天
    @staticmethod
    def get_week_end_day(current_day=None):
        if current_day is None:
            current_day = datetime.datetime.now()

        date = current_day - datetime.timedelta(days=current_day.weekday() - 6)
        return datetime.datetime(date.year, date.month, date.day, 0, 0, 0)

    @staticmethod
    def parse_str_to_date(time_str, format="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.strptime(time_str, format)


    # 获取两个时间相差天数
    @staticmethod
    def get_days_by_two_day(start_time, end_time):
        oneday = datetime.timedelta(days=1)
        count = 0
        while start_time != end_time:
            end_time = end_time - oneday
            count += 1
        return count

    # 获取两个时间范围段内的所有时间
    @staticmethod
    def get_dates_in_two_day(start_time, end_time):
        days = DateUtil.get_days_by_two_day(start_time, end_time)
        days += 1
        dates = []
        for n in range(0, days, 1):
            dates.append(DateUtil.add_day(n, start_time))
        return dates

    # 比较两个时间的大小  如果first_time 在 end_time 前面 返回true 反正返回false
    @staticmethod
    def compare_time(first_time, end_time):
        s_time = time.mktime(time.strptime(first_time, '%Y%m%d%H%M'))  # get the seconds for specify date
        e_time = time.mktime(time.strptime(end_time, '%Y%m%d%H%M'))
        if float(s_time) >= float(e_time):
            return True
        else:
            return False

    # 获取当前时间时间戳 精确到毫秒
    @staticmethod
    def get_current_time_stamp():
        return int(round(time.time() * 1000))

    # 获得几天前的时间戳
    def get_before_days_timestamp(self, start_time, before_days):
        b_days = timedelta(days = before_days)
        b_timestamp = b_days.total_seconds()*1000
        return start_time - b_timestamp

    # 时间戳转化成特定格式
    def return_format_datetime(self, datetime_timestamp, format_string = None):
        date_str = datetime.date.fromtimestamp(datetime_timestamp/1000)
        if None == format_string:
            format_string = '%Y-%m-%d %H:%M:%S'
        date_format_str = date_str.strftime(format_string)
        return date_format_str