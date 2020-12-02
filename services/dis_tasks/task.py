from services.dis_tasks.celery_con import app
import time


@app.task
def test(x, y):
    time.sleep(5)
    return x + y


@app.task
def scan(x,y):
    time.sleep(1)
    return x-y
