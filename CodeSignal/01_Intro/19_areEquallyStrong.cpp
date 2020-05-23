//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-5/g6dc9KJyxmFjB98dL

bool areEquallyStrong(int yourLeft, int yourRight, int friendsLeft, int friendsRight) {
    if (max(yourLeft, yourRight) == max(friendsLeft, friendsRight)) {
        if (min(yourLeft, yourRight) == min(friendsLeft, friendsRight)) {
            return true;
        }
    }
    return false;
}
