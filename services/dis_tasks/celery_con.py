from celery import Celery
import time


app = Celery(backend='amqp', broker='amqp://hunyuan:112352sx.@127.0.0.1:5672')

