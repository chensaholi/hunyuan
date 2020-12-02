from services.dis_tasks.task import test, scan


res = test.delay(2, 2)
print(res.get())
