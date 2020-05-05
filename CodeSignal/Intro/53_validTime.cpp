//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-12/ywMyCTspqGXPWRZx5

bool validTime(std::string time) {
    int h = stoi(time.substr(0, 2)), m = stoi(time.substr(3));
    return h >= 0 && h < 24 && m >= 0 && m < 60;
}
