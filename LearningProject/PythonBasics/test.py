#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
from django.utils import timezone

now = datetime.datetime.now()
nextNow = now + datetime.timedelta(hours=23, minutes=59)
nextNow2 = now + datetime.timedelta(days=1)
print(now)
print(nextNow)
print(nextNow2)