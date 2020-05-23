//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL

std::vector<std::string> allLongestStrings(std::vector<std::string> inputArray) {
    std::vector<std::string> outputArray;
    int max = 0;
    int len = 0;
    for (auto s : inputArray) {
        len = s.size();
        if (len > max) {
            max = len;
            outputArray.clear();
            outputArray.emplace_back(s);
        }
        else if (len == max) {
            outputArray.emplace_back(s);
        }
    }
    return outputArray;
}
