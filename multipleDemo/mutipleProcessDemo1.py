import multiprocessing
import time

class Producer(multiprocessing.Process):
    def __init__(self,queue):
        multiprocessing.Process.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            self._queue.put("time is %s" % time.time())
            time.sleep(5)

class Consumer(multiprocessing.Process):
    def __init__(self,queue, number):
        multiprocessing.Process.__init__(self)
        self._queue = queue
        self._number = number

    def run(self):
        while True:
            timeString = self._queue.get()
            print timeString,self._number

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    producer = Producer(queue)
    consumer1 = Consumer(queue,1)
    consumer2 = Consumer(queue,2)
    producer.start()
    consumer1.start()
    consumer2.start()
