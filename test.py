#!/usr/bin/env python
# coding:utf-8

from python_date_util import *

from nose.tools import assert_equal


class TestA(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_get_local_today(self):
        assert_equal(date_to_string(get_local_today()), '2015-07-28')

    def test_get_date_by_days_delta(self):
        assert_equal(date_to_string(get_date_by_days_delta(2)), '2015-07-26')

    def test_get_last_day(self):
        assert_equal(date_to_string(get_last_day(get_local_today())), '2015-07-27')

    def test_get_monday(self):
        assert_equal(date_to_string(get_monday(string_to_date('2015-07-31'))), '2015-07-27')

    def test_get_last_week_sunday(self):
        assert_equal(date_to_string(get_last_sunday(string_to_date('2015-07-31'))), '2015-07-26')

    def test_get_first_day_of_month(self):
        assert_equal(date_to_string(get_first_day_of_month(get_local_today())), '2015-07-01')

    def test_get_last_month_range(self):
        begin, end = get_last_month_range(get_local_today())
        assert_equal(date_to_string(begin), '2015-06-01')
        assert_equal(date_to_string(end), '2015-06-30')
