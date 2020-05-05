//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-12/fQpfgxiY6aGiGHLtv

int differentSquares(std::vector<std::vector<int>> matrix) {
    set<list<int>> squares;
    for (int x = 0; x < matrix.size() - 1; x++) {
        for (int y = 0; y < matrix[x].size() - 1; y++) {
            list<int> square;
            for (int a : {x, x + 1}) {
                for (int b : {y, y + 1}) {
                    square.push_back(matrix[a][b]);
                }
            }
            squares.insert(square);
        }
    }
    return squares.size();
}
