# CodeSignal SawSubArray solution, simple O(N) single pass solution

def saw(example):
    alternate = None  # Up is True, down is False
    result = 0
    index = 1
    while index < len(example):
        if example[index] != example[index - 1]:
            if alternate is None:
                alternate = bool(example[index] < example[index - 1])
            counter = 1
            l = 2
            index += 1
            while index < len(example):
                if (example[index] != example[index - 1]) and (bool(example[index] > example[index - 1]) == alternate):
                    counter += l
                    l += 1
                    alternate = not alternate
                    index += 1
                else:
                    break
            alternate = None
            result += counter
        else:
            index += 1
    return result

def main():
    # example = [1, 2, 1, 2, 1]  # 10
    # example = [1, 2, 1, 2, 1, 0, 0, 0, 3, 5, 4, 6, 6]  # 18
    example = [0, 0, 3, 5, 4, 6, 6]  # 7
    print("\nInput: {}\nResult: {}\n".format(example, saw(example)))

if __name__ == "__main__":
    main()