# https://realpython.com/python-concurrency/

import time
import concurrent.futures
import multiprocessing


def cpu_bound(number):
    return sum(i * i for i in range(number))

def synchronousTest(numbers):
    print("\nSynchronous CPU bound Assessments")
    startTime = time.time()
    for number in numbers:
        cpu_bound(number)
    duration = time.time() - startTime
    print("Duration: {}\n".format(duration))
    return duration

def threadingTest(numbers):
    print("Threading CPU bound Assessments")
    startTime = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound, numbers)
    duration = time.time() - startTime
    print("Duration: {}\n".format(duration))
    return duration

def multiprocessingTest(numbers):
    print("Multiprocessing CPU bound Assessments")
    startTime = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)
    duration = time.time() - startTime
    print("Duration: {}\n".format(duration))
    return duration

def main():
    numbers = [5000000 + x for x in range(10)]
    print("\nValues being tested: {}".format(numbers))
    s = synchronousTest(numbers)
    t = threadingTest(numbers)
    m = multiprocessingTest(numbers)
    print("Threading-Synchronous performance comparison: {:.3f}%".format(t / s * 100))
    print("Multiprocessing-Synchronous performance comparison: {:.3f}%\n".format(m / s * 100))


if __name__ == "__main__":
    main()
