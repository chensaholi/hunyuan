import addTask


if __name__ == '__main__':
    result = addTask.add.delay(5, 5)
    print("the result is: ", result)
