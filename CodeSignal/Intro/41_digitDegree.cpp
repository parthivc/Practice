//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-9/hoLtYWbjdrD2PF6yo

int digitDegree(int n) {
    int counter = 0;
    string num = to_string(n);
    while (num.length() != 1) {
        int sum = 0;
        for (char c : num) {
            sum += int(c) - 48;
        }
        num = to_string(sum);
        counter++;
    }
    return counter;
}
