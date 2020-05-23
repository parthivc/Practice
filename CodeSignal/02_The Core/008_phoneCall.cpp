//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/intro-gates/mZAucMXhNMmT7JWta

int phoneCall(int min1, int min2_10, int min11, int s) {
    if (s < min1) {
        return 0;
    }
    for (int i = 1; i < 10; ++i) {
        if (s < min1 + min2_10 * i) {
            return i;
        }
    }
    return 10 + (s - min1 - min2_10 * 9) / min11;
}
