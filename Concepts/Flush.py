# Example of printing a flushed output before and after

import sys, time


def main():
    n = 100
    print("\nWill count from 1 to {}\n".format(n))
    for i in range(1, n + 1):
        sys.stdout.write("\r#{} ".format(i))
        sys.stdout.flush()
        time.sleep(0.013)
    print("\n\nCounted to {}!\n".format(n))

if __name__ == "__main__":
    main()