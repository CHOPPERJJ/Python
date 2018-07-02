#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone
# 获取当前时间
now = datetime.now()
print('now = ', now)
print('type(now) =', type(now))

# 用指定日期时间创建datetime:
dt = datetime(2018, 7, 2, 14, 55)
print(dt)

# 把datetime转换为timestamp:
print('datetime -> timstamp:', dt.timestamp())

# 把timestamp转换为datetime:
t = dt.timestamp()
print('timestamp -> datetime:',datetime.fromtimestamp(t))
print('timestamp -> datetime UTC TIME:', datetime.utcfromtimestamp(t))

# str转换为datetime
cday = datetime.strptime('2018-07-02 15:16:00','%Y-%m-%d %H:%M:%S')
print('strptime:', cday)

# datetime转换为str
print('strftime:', cday.strftime('%a, %b %d %H:%M'))

# 对日期进行加减：
print('current datetime =', cday)
print('current + 10 hours =', cday + timedelta(hours=10))
print('current + 1days =', cday + timedelta(days=1))
print('current + 2.5days =', cday + timedelta(days=2, hours=12))

# 把时间从UTC+0时区转换为UTC+8：
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now=', utc_dt)
print('UTC+8:00 now=', utc8_dt)