//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-11/pwRLrkrNpnsbgMndb

bool isValid(int x, int y) {
    return x > 0 && x <= 8 && y > 0 && y <= 8;
}

int chessKnight(std::string cell) {
    int nFile = int(cell[0]) - 96, nRank = cell[1] - '0', moveCount = 0;
    for (int i : {-1, 1}) {
        for (int j : {-1, 1}) {
            if (isValid(nFile + 2 * i, nRank + j)) {
                moveCount++;
            }
            if (isValid(nFile + i, nRank + 2 * j)) {
                moveCount++;
            }
        }
    }
    return moveCount;
}
