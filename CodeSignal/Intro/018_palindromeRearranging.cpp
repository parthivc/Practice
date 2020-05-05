//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico

bool palindromeRearranging(std::string inputString) {
    map<char, int> count;
    for (char c : inputString) {
        if (count[c]) {
            count[c] += 1;
        }
        else {
            count[c] = 1;
        }
    }
    int oddCounter = 0;
    for (auto it : count) {
        if (it.second % 2) {  // Odd
            oddCounter++;
        }
    }
    return oddCounter < 2;
}
