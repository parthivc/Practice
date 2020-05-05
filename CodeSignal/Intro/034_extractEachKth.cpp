//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R

std::vector<int> extractEachKth(std::vector<int> inputArray, int k) {
    k -= 1;
    int index = k;
    auto it = inputArray.begin();
    while (index < inputArray.size()) {
        inputArray.erase(it + index);
        index += k;
    }
    return inputArray;
}
