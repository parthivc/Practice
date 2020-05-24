//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/7jaup9HprdJno2diw

bool tennisSet(int score1, int score2) {
    return ((max(score1, score2) == 6 and min(score1, score2) < 5) || (min(score1, score2) >= 5 && min(score1, score2) <= 6 && max(score1, score2) == 7));
}
