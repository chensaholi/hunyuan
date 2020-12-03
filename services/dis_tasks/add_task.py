# -*- coding: utf-8 -*-
# addTask.py: Executing a simple task
from celery import Celery
import time


app = Celery('addTask', broker='amqp://hunyuan:112352sx.@127.0.0.1:5672')


@app.task
def add(x, y):
    time.sleep(4)
    return x + y

