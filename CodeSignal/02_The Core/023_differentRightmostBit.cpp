//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/whz5JzszYTdXW6aNA

int differentRightmostBit(int n, int m) {
    return -~((~(n ^ m)) ^ ((~(n ^ m)) + 1)) / 2;
}
