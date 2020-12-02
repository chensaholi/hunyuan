#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# task.py for windows

import time, sys, queue, random
from multiprocessing.managers import BaseManager

BaseManager.register('get_task')
BaseManager.register('get_result')

conn = BaseManager(address=('127.0.0.1', 5002), authkey=b'123')

try:
    conn.connect()
except:
    print('连接失败')
    sys.exit()

task = conn.get_task()
result = conn.get_result()

while not task.empty():
    n = task.get(timeout = 1)
    print('run task %d' % n)
    sleeptime = random.randint(0,3)
    time.sleep(sleeptime)
    rt = (n, sleeptime)
    result.put(rt)
