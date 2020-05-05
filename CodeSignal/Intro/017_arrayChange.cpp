//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg

int arrayChange(std::vector<int> inputArray) {
    int count = 0;
    for (int index = 1; index < inputArray.size(); index++) {
        for (int change = inputArray[index]; change < inputArray[index - 1] + 1; change++) {
            inputArray[index]++;
            count++;
        }
    }
    return count;
}
