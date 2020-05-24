//
// Created by Parthiv Chigurupati on 5/23/20.
//

// Problem Statement: https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/J7PQDxpWqhx7HrvBZ

std::vector<int> metroCard(int lastNumberOfDays) {
    switch (lastNumberOfDays) {
        case 28:
        case 30:
            return {31};
        case 31:
            return {28, 30, 31};
    }
}
