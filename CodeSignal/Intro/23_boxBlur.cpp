//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP

std::vector<std::vector<int>> boxBlur(std::vector<std::vector<int>> image) {
    int width = image.size() - 2, height = image[0].size() - 2;
    vector<vector<int>> blurredImage;
    for (int startX = 0; startX < width; startX++) {
        blurredImage.emplace_back(vector<int>());
        for (int startY = 0; startY < height; startY++) {
            int sum = 0;
            for (int x = startX; x < startX + 3; x++) {
                for (int y = startY; y < startY + 3; y++) {
                    sum += image[x][y];
                }
            }
            blurredImage[startX].emplace_back(sum / 9);
        }
    }
    return blurredImage;
}
