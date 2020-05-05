//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE

int arrayMaximalAdjacentDifference(std::vector<int> inputArray) {
    int maxVal = INT_MIN;
    for (int index = 1; index < inputArray.size(); index++) {
        maxVal = max(maxVal, abs(inputArray[index] - inputArray[index - 1]));
    }
    return maxVal;
}
