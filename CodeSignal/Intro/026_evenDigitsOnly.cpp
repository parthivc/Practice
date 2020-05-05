//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-6/6cmcmszJQr6GQzRwW

bool evenDigitsOnly(int n) {
    for (char c : to_string(n)) {
        if (int(c) % 2) {
            return false;
        }
    }
    return true;
}
