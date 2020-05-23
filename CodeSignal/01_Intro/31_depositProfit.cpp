//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-7/8PxjMSncp9ApA4DAb

int depositProfit(int deposit, int rate, int threshold) {
    double val = deposit * 1.0, percentage = rate / 100.0 + 1.0;
    int counter = 0;
    while (val < threshold) {
        val *= percentage;
        counter++;
    }
    return counter;
}
