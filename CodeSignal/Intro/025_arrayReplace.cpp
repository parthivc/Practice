//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm

std::vector<int> arrayReplace(std::vector<int> inputArray, int elemToReplace, int substitutionElem) {
    for (int index = 0; index < inputArray.size(); index++) {
        if (inputArray[index] == elemToReplace) {
            inputArray[index] = substitutionElem;
        }
    }
    return inputArray;
}
