import concurrent.futures
import logging
import queue
import random
import threading
import time


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


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    pipeline = queue.Queue(maxsize=20)  # Threadsafe queue for tasks, size can be changed proportionally
    event = threading.Event()  # Threading event used to end the task
    startTime = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:  # One worker for each process
        executor.submit(producer, pipeline, event)  # Starts the producer
        executor.submit(consumer, pipeline, event)  # Starts the consumer
        time.sleep(0.1)  # Runs the task for a set amount of time
        logging.info("Main: about to set event")
        event.set()  # Sets the event and ends all of the processes
    duration = time.time() - startTime
    print("\nDuration: {:.4f} seconds\n".format(duration))


if __name__ == "__main__":
    main()
