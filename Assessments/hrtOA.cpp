//
// Created by Parthiv Chigurupati on 10/11/20.
//



#include <iostream>
#include <queue>
#include <algorithm>


using namespace std;

void question1(vector<int> &A) {
    long total = 0;
    int sum = 0;
    int size = A.size();
    priority_queue<int> negatives;
    for (int i = 0; i < size; ++i) {
        total += A[i];
        if (A[i] < 0) {  // Negative value
            // Add to maxheap and multiply for -1 so minheap pops largest value
            negatives.push(-A[i]);  // Value, index
            while (total < 0 && !negatives.empty()) {
                total += negatives.top();
                negatives.pop();
                sum += 1;
            }
        }
    }
    cout << sum << endl;
}

struct value {
    int val, x, y;
};

bool compatible(value a, value b) {
    return (a.x != b.x && a.y != b.y);
}

bool compareValues(value a, value b) {
    return (a.val > b.val);
}

void question2(vector<vector<int>> &A) {
    int n = A.size();
    int m = A[0].size();
    int result = 0;
    vector<value> values(n * m);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            values[i * m + j] = value{A[i][j], i, j};
        }
    }
    sort(values.begin(), values.end(), compareValues);
    for (int i = 0; i < n * m - 1; ++i) {
        if (values[i].val + values[i + 1].val <= result) {
            break;
        }
        for (int j = 0; j < n * m - 1; ++j) {
            if (compatible(values[i], values[j])) {
                result = max(result, values[i].val + values[j].val);
                break;
            }
        }
    }
    cout << result << endl;
}

struct house {
    int x, y;
};

int dist(house a, int x, int y) {
    return abs(a.x - x) + abs(a.y - y);
}

bool same(house a, int x, int y) {
    return (a.x == x && a.y == y);
}

void question3(int K, vector<vector<int>> &A) {
    int n = A.size();
    int m = A[0].size();
    house e[] = {{-1, -1}, {-1, m}, {n, -1}, {n, m}};  // locations of extremes
    house c[4];
    int dists[4];
    fill(dists, dists + 4, n + m + 4);
    // top right, top left, bottom right, bottom left
    vector<house> houses;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (A[i][j]) {
                struct house current = {i, j};
                houses.emplace_back(current);
                for (int h = 0; h < 4; ++h) {
                    if (dist(e[h], i, j) < dists[h]) {
                        dists[h] = dist(e[h], i, j);
                        c[h] = current;
                    }
                }
            }
        }
    }
    int result = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            bool flag = true;
            for (house h : c) {
                if (dist(h, i, j) > K || same(h, i, j)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                for (house h : houses) {
                    if (dist(h, i, j) > K || same(h, i, j)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    result += 1;
                }
            }
        }
    }
    cout << result << endl;
}

int hrtOA() {
//    question1();
//    question2();
//    question3();
    return 0;
}
