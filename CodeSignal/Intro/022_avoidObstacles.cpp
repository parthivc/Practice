//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5

int avoidObstacles(std::vector<int> inputArray) {
    for(int len = 1; len <= *max_element(inputArray.begin(), inputArray.end()); len++) {
        bool hit = false;
        for (int i : inputArray) {
            if (!(i % len)) {
                hit = true;
                break;
            }
        }
        if (!hit) {
            return len;
        }
    }
    return *max_element(inputArray.begin(), inputArray.end()) + 1;
}

