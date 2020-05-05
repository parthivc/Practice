//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN

std::vector<std::string> addBorder(std::vector<std::string> picture) {
    std::vector<std::string> returnVal;
    int len = picture[0].length() + 2;
    returnVal.emplace_back(std::string(len, '*'));
    for (std::string s : picture) {
        returnVal.emplace_back("*" + s + "*");
    }
    returnVal.emplace_back(std::string(len, '*'));
    return returnVal;
}
