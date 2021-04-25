# This script demonstrates what a race condition could impact
# While the result isn't obvious, the issue is that counter is not protected
# This means that the system might read the value, switch threads, and add one to it
# This would cause the addition to be performed on an old value

import concurrent.futures

counter = 0

def increment_counter(fake_value):
    global counter
    for _ in range(100):
        counter += 1


if __name__ == "__main__":
    fake_data = [x for x in range(5000)]
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5000) as executor:
        executor.map(increment_counter, fake_data)
    print("\nCounter: \t\t{}\nExpected Counter: \t{}\n".format(counter, 100 * 5000))
