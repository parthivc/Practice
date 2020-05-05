//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-7/ZFnQkq9RmMiyE6qtq

int absoluteValuesSumMinimization(std::vector<int> a) {
    if (a.size() % 2) {  // Odd Length
        return a[a.size() / 2];
    }
    else {
        return a[a.size() / 2 - 1];
    }
}
