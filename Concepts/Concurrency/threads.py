# https://realpython.com/intro-to-python-threading/

import logging
import concurrent.futures
import queue
import random
import threading
import time

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    logging.info("Thread %s: finishing", name)

def threadLockTest():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)
    database = FakeDatabase()
    logging.info(
        "Testing locked update. Starting value is %d.", database.value
    )
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info("Testing locked update. Ending value is %d.", database.value)

def daemonThreadTest():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")

def raceConditionTest():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d. Expected value is 2", database.value)

SENTINEL = object()  # Replacement for `None` when `None` is a useful value

def pipelineTest():
    def producer(queue, event):
        """Pretend we're getting a number from the network."""
        while not event.is_set():
            message = random.randint(1, 101)
            logging.info("Producer got message: %s", message)
            queue.put(message)
        logging.info("Producer received event. Exiting")

    def consumer(queue, event):
        """Pretend we're saving a number in the database."""
        while not event.is_set() or not queue.empty():
            message = queue.get()
            logging.info(
                "Consumer storing message: %s (size=%d)", message, queue.qsize()
            )

        logging.info("Consumer received event. Exiting")

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    pipeline = queue.Queue(maxsize=5)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()

# Semaphores are locks that have an internal counter
# This counter restricts the number of objects that can access a shared resource at any given time (load-limiting)

# Threading barriers require that a minimum number of threads are active to proceed
# This is useful if you don't want a process to start unless all threads have been spawned

def main():
    print("\nThreadlock test")
    threadLockTest()
    print("\nDaemon thread test")  # Daemon threads are killed after completed instead of internally running thread.shutdown like normal threads
    daemonThreadTest()
    print("\nRace condition test")
    raceConditionTest()
    print("\nPipeline producer-consumer lock test")
    pipelineTest()
    print()


if __name__ == "__main__":
    main()
