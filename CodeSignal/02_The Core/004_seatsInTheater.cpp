//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/intro-gates/bszFiQAog96G9CXKg

int seatsInTheater(int nCols, int nRows, int col, int row) {
    return (nRows - row) * (nCols - col + 1);
}
