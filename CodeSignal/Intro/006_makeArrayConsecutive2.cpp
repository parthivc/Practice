//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

int makeArrayConsecutive2(std::vector<int> statues) {
    sort(statues.begin(), statues.end());
    return statues[statues.size() - 1] - statues[0] - statues.size() + 1;
}
