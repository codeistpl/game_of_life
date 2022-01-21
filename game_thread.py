from threading import Thread
from time import sleep


class GameThread(Thread):
    def __init__(self, target=None, args=()):
        Thread.__init__(self, target=self.loop)
        self.keep_going = True
        self.target = target
        self.args = args

    def loop(self):
        while self.keep_going:
            self.target(*self.args)
            sleep(1)

    def stop(self):
        self.keep_going = False
