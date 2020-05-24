//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/r9azLYp2BDZPyzaG2

int knapsackLight(int value1, int weight1, int value2, int weight2, int maxW) {
    if (weight1 + weight2 <= maxW) {
        return value1 + value2;
    }
    else if (weight1 <= maxW) {
        if (weight2 <= maxW) {
            return max(value1, value2);
        }
        else {
            return value1;
        }
    }
    else if (weight2 <= maxW) {
        return value2;
    }
    else {
        return 0;
    }
}
