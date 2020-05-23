//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-9/6M57rMTFB9MeDeSWo

bool bishopAndPawn(std::string bishop, std::string pawn) {
    int bFile = int(bishop[0]) - 64, bRank = int(bishop[1]), pFile = int(pawn[0]) - 64, pRank = int(pawn[1]);
    return abs(bFile - pFile) == abs(bRank - pRank);
}
