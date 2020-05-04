//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ

int shapeArea(int n) {
    if (n == 1) {
        return n;
    }
    return shapeArea(n - 1) + 2 * n + 2 * (n - 2);
}
