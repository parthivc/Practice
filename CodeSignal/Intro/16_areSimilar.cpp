//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP

bool areSimilar(std::vector<int> a, std::vector<int> b) {
    if (a == b) {
        return true;
    }
    int i = 0;
    while (i < a.size()) {
        if (a[i] == b[i]) {
            a.erase(a.begin() + i);
            b.erase(b.begin() + i);
        }
        else {
            i++;
        }
    }
    if (a.size() != 2) {
        return false;
    }
    reverse(b.begin(), b.end());
    return a == b;
}
