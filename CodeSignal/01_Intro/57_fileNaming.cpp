//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-12/sqZ9qDTFHXBNrQeLC

std::vector<std::string> fileNaming(std::vector<std::string> names) {
    map<string, int> counts;
    vector<string> newNames;
    for (string s : names) {
        if (counts[s]) {
            string newName = s + '(' + to_string(counts[s]) + ')';

            while (counts[newName]) {
                counts[s] += 1;
                newName = s + '(' + to_string(counts[s]) + ')';
            }
            if (!counts[newName]) {
                counts[newName] = 1;
            }
            counts[s] += 1;
            newNames.emplace_back(newName);
        }
        else {
            counts[s] = 1;
            newNames.emplace_back(s);
        }
    }
    return newNames;
}
