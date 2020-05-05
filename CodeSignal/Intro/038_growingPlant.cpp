//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-9/xHvruDnQCx7mYom3T

int growingPlant(int upSpeed, int downSpeed, int desiredHeight) {
    if (upSpeed >= desiredHeight) {
        return 1;
    }
    int dailyGrowth = upSpeed - downSpeed;
    return max(max((desiredHeight - upSpeed) / dailyGrowth, 1) + 1, 1);
}
