//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-12/s9qvXv4yTaWg8g4ma

#include <regex>
std::string longestWord(std::string text) {
    regex pattern("[a-zA-Z]+");
    auto textBegin = sregex_iterator(text.begin(), text.end(), pattern);
    auto textEnd = sregex_iterator();
    int maxLen = 0;
    string maxWord = "";
    for (auto k = textBegin; k != textEnd; k++) {
        smatch match = *k;
        string word = match.str();
        if (word.length() > maxLen) {
            maxLen = word.length();
            maxWord = word;
        }
    }
    return maxWord;
}
