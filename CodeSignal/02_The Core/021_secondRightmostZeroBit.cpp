//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/9nSj6DgqLDsBePJha

int secondRightmostZeroBit(int n) {
    return -~((n - ~(n ^ (n + 1)) / 2) ^ (n - ~(n ^ (n + 1)) / 2 + 1)) / 2;
}
