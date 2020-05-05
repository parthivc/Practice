//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui

std::string alphabeticShift(std::string inputString) {
    string shifted = "";
    int val;
    for (char c : inputString) {
        val = int(c) + 1;
        if (val == 91 || val == 123) {
            val -= 26;
        }
        shifted += char(val);
    }
    return shifted;
}
