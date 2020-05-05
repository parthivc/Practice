//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno

#include <regex>
bool variableName(std::string name) {
    regex nameMatch("^[a-zA-Z_][a-zA-Z_0-9]*$");
    return regex_match(name.begin(), name.end(), nameMatch);
}
