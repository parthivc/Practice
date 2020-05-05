//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9

std::vector<int> alternatingSums(std::vector<int> a) {
    int sum1 = 0, sum2 = 0;
    for (int index = 0; index < a.size(); index++) {
        if (index % 2) {
            sum2 += a[index];
        }
        else {
            sum1 += a[index];
        }
    }
    std::vector<int> rVal = {sum1, sum2};
    return rVal;
}
