//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/intro-gates/aiKck9MwwAKyF8D4L

int lateRide(int n) {
    return (n / 600) + (n / 60) % 10 + (n % 60) / 10 + (n % 60) % 10;
}
