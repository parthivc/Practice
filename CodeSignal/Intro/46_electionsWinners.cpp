//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-10/8RiRRM3yvbuAd3MNg

int electionsWinners(std::vector<int> votes, int k) {
    int maxCount = *max_element(votes.begin(), votes.end()), winnerCount = 0;
    if (!k) {
        return count(votes.begin(), votes.end(), maxCount) == 1;
    }
    for (int v : votes) {
        if (v + k > maxCount) {
            winnerCount++;
        }
    }
    return winnerCount;
}
