//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/KeMqde6oqfF5wBXxf

int arrayPacking(std::vector<int> a) {
    int packed = 0;
    for (int i = 0; i < a.size(); ++i) {
        packed += a[i] << 8 * i;
    }
    return packed;
}
