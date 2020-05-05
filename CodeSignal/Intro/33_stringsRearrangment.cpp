//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9

bool oneDiff(string &a, string &b) {
    int counter = 0;
    for (int index = 0; index < a.length(); index++) {
        if (a[index] != b[index]) {
            counter++;
        }
    }
    return counter == 1;
}

bool stringsRearrangement(std::vector<std::string> inputArray) {
    vector<vector<string>> permutations;
    sort(inputArray.begin(), inputArray.end());
    do {
        permutations.emplace_back(inputArray);
    } while (next_permutation(inputArray.begin(),inputArray.end()));
    for (vector<string> permutation : permutations) {
        bool unbroken = true;
        for (int index = 0; index < permutation.size() - 1; index++) {
            if (!oneDiff(permutation[index], permutation[index + 1])) {
                unbroken = false;
                break;
            }
        }
        if (unbroken) {
            return true;
        }
    }
    return false;
}
