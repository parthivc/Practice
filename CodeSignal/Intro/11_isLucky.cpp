//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ

bool isLucky(int n) {
    std::string num = std::to_string(n);
    int halfLen = num.length() / 2, firstSum = 0, lastSum = 0;
    for (int index = 0; index < halfLen; index++) {
        firstSum += int(num[index]);
        lastSum += int(num[index + halfLen]);
    }
    return firstSum == lastSum;
}
