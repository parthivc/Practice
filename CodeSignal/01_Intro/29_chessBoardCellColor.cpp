//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi

bool chessBoardCellColor(std::string cell1, std::string cell2) {
    int sum1 = int(cell1[0]) - 64 + int(cell1[1]), sum2 = int(cell2[0]) - 64 + int(cell2[1]);
    return sum1 % 2 == sum2 % 2;
}
