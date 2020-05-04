//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ

bool checkPalindrome(std::string inputString) {
    int len = inputString.length();
    for (int index = 0; index < len / 2 + 1; index++) {
        if (inputString[index] != inputString[len - index - 1]) {
            return false;
        }
    }
    return true;
}
