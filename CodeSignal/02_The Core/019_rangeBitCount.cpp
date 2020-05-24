//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/eC2Zxu5H5SnuKxvPT

int rangeBitCount(int a, int b) {
    int count = 0;
    for (int i = a; i <= b; ++i) {
        int holder = i;
        while (holder) {
            if(holder & 1) {
                ++count;
            }
            holder >>= 1;
        }
    }
    return count;
}
