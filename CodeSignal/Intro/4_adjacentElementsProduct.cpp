//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m

int adjacentElementsProduct(std::vector<int> inputArray) {
    int max = inputArray[0] * inputArray[1];
    for (int index = 2; index < inputArray.size(); index++) {
        if (inputArray[index - 1] * inputArray[index] > max) {
            max = inputArray[index - 1] * inputArray[index];
        }
    }
    return max;
}
