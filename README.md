## Introduction

一些方面使用的日期处理方面的函数，例如
- get_local_now, 获取时区是当前时区的now
- delta_to_days, 时间差转换为天数
- delta_to_hours, 时间差转换为小时数
- get_monday, 获取指定日期所在星期的周一
- get_last_sunday， 获取指定日期所在星期的上个周日
- get_last_week_range, 获取指定日期的上周周一到周日，方便做统计等一些工作时使用
- get_last_month_range, 获取指定日期所在月上一个月的第一天和最后一天

## Requirements

依赖于python-dateutil, 需先`pip install python-dateutil==1.5`
