import threading

class MyThread(threading.Thread):
    def __init__(self, arg1, arg2):
        threading.Thread.__init__(self)
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self):
        pass

