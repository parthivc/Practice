//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-10/HJ2thsvjL25iCvvdm

#include <regex>
bool isMAC48Address(std::string inputString) {
    regex pattern("^([0-9A-F]{2}-){5}[0-9A-F]{2}$");
    return regex_match(inputString, pattern);
}
