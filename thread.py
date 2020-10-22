from threading import Thread
from threading import Lock
import time

class MyThread(Thread):
    def __init__(self, thread_id, name, delay):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting :{}".format(self.name))
        print_thd(self.delay)

def print_thd(delay):
    counter = 5
    while counter:
        print("Sleeping :{}".format(time.sleep(10)))
        counter -= 1

th1 = MyThread(1, "Thread1", 10)
th2 = MyThread(2, "Thread2", 10)

th1.start()
th2.start()