//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-12/uRWu6K8E7uLi3Qtvx

std::vector<std::vector<int>> spiralNumbers(int n) {
    vector<vector<int>> spiral(n, vector<int>(n));
    int leftBound = 0, rightBound = n, counter = 0, x, y;
    while (rightBound - leftBound > 0) {
        for (y = leftBound; y < rightBound; ++y) {
            spiral[leftBound][y] = ++counter;
        }
        --y;
        for (x = leftBound + 1; x < rightBound; ++x) {
            spiral[x][y] = ++counter;
        }
        --x;
        for (y -= 1; y >= leftBound; --y) {
            spiral[x][y] = ++counter;
        }
        ++y;
        for (x -= 1; x > leftBound; --x) {
            spiral[x][y] = ++counter;
        }
        leftBound++, rightBound--;
    }
    return spiral;
}
