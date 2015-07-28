#!/usr/bin/env python
# coding:utf-8

import datetime

import dateutil.tz
local_zone = dateutil.tz.tzlocal()


def get_local_now():
    return datetime.datetime.now().replace(tzinfo=local_zone)


def get_local_today():
    return get_local_now().date()


def change_to_local_zone(dt):
    return dt.astimezone(local_zone)
#-------------------------------------------------------------------------------


def datetime_to_string(dt, format='%Y-%m-%d %H:%M:%S'):
    return dt.astimezone(local_zone).strftime(format)


def date_to_string(dt, format='%Y-%m-%d'):
    return dt.strftime(format)


def get_now_str():
    return datetime_to_string(get_local_now())


def string_to_datetime(s, format='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.strptime(s, format).replace(tzinfo=local_zone)


def string_to_date(s, format='%Y-%m-%d'):
    return datetime.datetime.strptime(s, format).replace(tzinfo=local_zone).date()
#-------------------------------------------------------------------------------


def get_date_by_days_delta(days):
    return get_local_now() - datetime.timedelta(days=days)


def delta_to_days(delta):
    return delta.days + delta.seconds / (24 * 3600 * 1.0)


def delta_to_hours(delta):
    return delta.days * 24 + delta.seconds // 3600
#-------------------------------------------------------------------------------


def get_last_day(date):
    return date - datetime.timedelta(days=1)


def get_monday(date):
    return date - datetime.timedelta(days=date.isoweekday() - 1) if date.isoweekday() > 1 else date


def get_last_sunday(date):
    return date - datetime.timedelta(days=date.isoweekday())


def get_last_week_range(date):
    last_sunday = get_last_sunday(date)
    last_monday = get_monday(last_sunday)
    return last_monday, last_sunday


def get_first_day_of_month(date):
    return datetime.date(date.year, date.month, 1)


def get_last_month_range(date):
    first_day_of_this_month = get_first_day_of_month(date)
    last_day_of_last_month = first_day_of_this_month - datetime.timedelta(days=1)
    first_day_of_last_month = get_first_day_of_month(last_day_of_last_month)
    return first_day_of_last_month, last_day_of_last_month
