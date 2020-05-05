//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-9/AACpNbZANCkhHWNs3

std::string longestDigitsPrefix(std::string inputString) {
    int len = 0;
    for (char c : inputString) {
        if (int(c) < 48 || int(c) > 57) {
            break;
        }
        len++;
    }
    return inputString.substr(0, len);
}
