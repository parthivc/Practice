//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-12/NJJhENpgheFRQbPRA

int digitsProduct(int product) {
    if (!product) {
        return 10;
    }
    else if (product == 1) {
        return 1;
    }
    int result = 0, digit = 1;
    for (int num = 9; num > 1; num--) {
        while (!(product % num)) {
            result += num * digit;
            digit *= 10;
            product /= num;
        }
    }
    if (product > 1) {
        return -1;
    }
    return result;
}
