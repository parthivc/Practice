//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-8/Rqvw3daffNE7sT7d5

int arrayMaxConsecutiveSum(std::vector<int> inputArray, int k) {
    int sum = 0;
    for (int index = 0; index < k; index++) {
        sum += inputArray[index];
    }
    int maxVal = sum;
    for (int index = k; index < inputArray.size(); index++) {
        sum += inputArray[index] - inputArray[index - k];
        if (sum > maxVal) {
            maxVal = sum;
        }
    }
    return maxVal;
}
