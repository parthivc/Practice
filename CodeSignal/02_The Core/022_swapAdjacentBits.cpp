//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/dShYZZT4WmvpmfpgB

int swapAdjacentBits(int n) {
    return (((n & 0x2AAAAAAA) >> 1) | ((n & 0x15555555) << 1));
}
