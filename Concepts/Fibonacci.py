

def constantFibonacci(n):
    sqrt5 = 5 ** 0.5
    phi = (sqrt5 + 1) / 2
    return round((phi ** n) / sqrt5)


def iterativeFibonacci(n):
    a = 0
    b = 1
    c = 1
    if n < 2:
        return n
    counter = 1
    while counter < n:
        c = a + b
        a = b
        b = c
        counter += 1
    return c


def main():
    print()
    for x in range(10):
        print(constantFibonacci(x))
    print()
    for x in range(10):
        print(iterativeFibonacci(x))
    print()


if __name__ == "__main__":
    main()
