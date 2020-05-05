//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-12/tQgasP8b62JBeirMS

bool sudoku(std::vector<std::vector<int>> grid) {
    for (int x = 0; x < 9; x++) {
        if (!(x % 3)) { // Check subgrids every 3 rows
            for (int s = 0; s < 9; s += 3) {  // Check each subgrid
                set<int> subgrid;
                for (int i = x; i < x + 3; i++) {
                    for (int j = s; j < s + 3; j++) {
                        subgrid.insert(grid[i][j]);
                    }
                }
                if (subgrid.size() != 9) {
                    return false;
                }
            }
        }
        set<int> line(grid[x].begin(), grid[x].end());
        if (line.size() != 9) {
            return false;
        }
        line.clear();
        for (int y = 0; y < 9; y++) {
            line.insert(grid[y][x]);
        }
        if (line.size() != 9) {
            return false;
        }
    }
    return true;
}
