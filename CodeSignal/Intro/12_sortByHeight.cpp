//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM

std::vector<int> sortByHeight(std::vector<int> a) {
    vector<int> returnVector = a;
    sort(a.begin(), a.end());
    int referenceIndex = 0;
    while (true) {
        if (a[referenceIndex] != -1) {
            break;
        }
        referenceIndex++;
    }
    for (int index = 0; index < returnVector.size(); index++) {
        if (returnVector[index] != -1) {
            returnVector[index] = a[referenceIndex++];
        }
    }
    return returnVector;
}
