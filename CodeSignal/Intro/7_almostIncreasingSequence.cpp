//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG

// returns the first index of a non-increasing pair, -1 if none
int helper(std::vector<int> check, int len, int i) {
    printf("Bad Index: %d\n", i);
    if (i > 0 && i < len) {
        if (check[i - 1] >= check[i + 1]) {
            return i - 1;
        }
    }
    for (int index = i + 1; index < len; index++) {
        if (check[index] >= check[index + 1]) {
            return index;
        }
    }
    return -1;
}

bool almostIncreasingSequence(std::vector<int> sequence) {
    int len = sequence.size() - 1;
    int badIndex = helper(sequence, len, -1); // Initial call, checking if a bad pair exists
    printf("Bad Index: %d\n", badIndex);
    if (badIndex == -1 || helper(sequence, len, badIndex) == -1 || helper(sequence, len, badIndex + 1) == -1) {
        return true;
    }
    return false;
}
