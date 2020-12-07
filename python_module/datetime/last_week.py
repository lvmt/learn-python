#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''计算上周星期几是几号.
'''


from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()

    day_num = start_date.weekday()  # 计算得到今天周几.

    day_num_target = weekdays.index(dayname) # 我们想查找上周几
    
    #days_ago = (7 + day_num - day_num_target) % 7
    days_ago = (7 - (day_num_target - day_num)) # 优化代码如下所示.

    # if days_ago == 0:
    #     days_ago = 7

    target_date = start_date - timedelta(days=days_ago)
    return target_date


for w in weekdays:
    print(w,get_previous_byday(w), sep=':\t\t')