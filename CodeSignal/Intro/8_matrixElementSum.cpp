//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr

int matrixElementsSum(std::vector<std::vector<int>> matrix) {
    int sum = 0, len = matrix[0].size();
    std::vector<int> validColumn = matrix[0];
    for (int x = 0; x < matrix.size(); x++) {
        for (int y = 0; y < matrix[x].size(); y++) {
            if (validColumn[y]) {
                if (matrix[x][y]) {
                    sum += matrix[x][y];
                }
                else {
                    validColumn[y] = 0;
                }
            }
        }
    }
    return sum;
}
