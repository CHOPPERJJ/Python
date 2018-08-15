#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading


# 新线程执行代码
def loop():
    # LoopThread子线程运行
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


# MainThread主线程运行
print('thread %s is running...' % threading.current_thread().name)
# 创建实例子进程
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
