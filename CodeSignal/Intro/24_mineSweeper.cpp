//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM

std::vector<std::vector<int>> minesweeper(std::vector<std::vector<bool>> matrix) {
    int height = matrix.size(), width = matrix[0].size();
    vector<vector<int>> mineMap (height, vector<int>(width, 0));
    vector<int> aList = {1, 1, 1, 0, 0, -1, -1, -1}, bList = {-1, 0, 1, -1, 1, -1, 0, 1};
    cout << height << " " << width << endl;
    for (int x = 0; x < height; x++) {
        for (int y = 0; y < width; y++) {
            int sum = 0;
            for (int index = 0; index < 8; index++) {
                int a = aList[index] + x, b = bList[index] + y;
                if (a > -1 && a < height && b > -1 && b < width && matrix[a][b]) {
                    sum += 1;
                }
            }
            mineMap[x][y] = sum;
        }
    }
    return mineMap;
}
