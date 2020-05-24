//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/e3zfPNTwTa9qTQzcX

int mirrorBits(int a) {
    int mirrored = 0;
    while (a > 0) {
        mirrored <<= 1;
        mirrored |= a & 1;
        a >>= 1;
    }
    return mirrored;
}
