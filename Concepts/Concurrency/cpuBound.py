# https://realpython.com/python-concurrency/

import time

def synchronousTest(numbers):
    def cpu_bound(number):
        return sum(i * i for i in range(number))

    print("\nSynchronous test")
    startTime = time.time()
    for number in numbers:
        cpu_bound(number)
    duration = time.time() - startTime
    print("Duration: {}\n".format(duration))


def main():
    numbers = [5000000 + x for x in range(10)]
    print(numbers)
    synchronousTest(numbers)


if __name__ == "__main__":
    main()
