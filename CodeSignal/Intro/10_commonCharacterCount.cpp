//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32

#include <cmath>

map<char, int> characterCount(std::string s) {
    map<char, int> counts;
    for (auto letter : s) {
        if (counts[letter]) {
            counts[letter]++;
        }
        else {
            counts[letter] = 1;
        }
    }
    return counts;
}

int commonCharacterCount(std::string s1, std::string s2) {
    map<char, int> m1 = characterCount(s1), m2 = characterCount(s2);
    int commonCount = 0;
    for (std::pair<char, int> i : m1) {
        printf("Letter: %c\tCount: %d\n", i.first, i.second);
        if (m2[i.first]) {
            commonCount += min(m1[i.first], m2[i.first]);
        }
    }
    return commonCount;
}
