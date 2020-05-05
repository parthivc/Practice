//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-12/YqZwMJguZBY7Hz84T

#include <regex>
int sumUpNumbers(std::string inputString) {
    regex pattern("\\d+");
    auto start = sregex_iterator(inputString.begin(), inputString.end(), pattern);
    auto end = sregex_iterator();
    int sum = 0;
    for (auto k = start; k != end; k++) {
        smatch match = *k;
        sum += stoi(match.str());
    }
    return sum;
}
