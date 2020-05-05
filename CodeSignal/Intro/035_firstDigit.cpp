//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-8/rRGGbTtwZe2mA8Wov

char firstDigit(std::string inputString) {
    for (char c : inputString) {
        if (int(c) >= 48 && int(c) <= 57) {
            return c;
        }
    }
}
