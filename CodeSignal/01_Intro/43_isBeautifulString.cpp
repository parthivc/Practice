//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-10/PHSQhLEw3K2CmhhXE

bool isBeautifulString(std::string inputString) {
    map<char, int> counts;
    for (int index = 65; index < 91; index++) {
        counts[char(index)] = 0;
    }
    for (char c : inputString) {
        counts[c]++;
    }
    for (auto it : counts) {
        char key = it.first;
        if (key != 'a' && counts[key] > counts[int(key) - 1]) {
            return false;
        }
    }
    return true;
}
