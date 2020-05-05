//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-11/vpfeqDwGZSzYNm2uX

int deleteDigit(int n) {
    string num = to_string(n);
    int maxVal = stoi(num.substr(1));
    for (int index = 1; index < num.length(); index++) {
        string str = num;
        str.erase(str.begin() + index);
        maxVal = max(maxVal, stoi(str));
    }
    return maxVal;
}
