# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import time


def rec_fib(num):
    if num == 0 or num == 1:
        return num
    return rec_fib(num-2) + rec_fib(num-1)


print('Hello World!')
while True:
    print(datetime.datetime.now())
    print(rec_fib(35))
    time.sleep(1)
