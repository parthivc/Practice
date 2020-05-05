//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-8/8N7p3MqzGQg5vFJfZ

int differentSymbolsNaive(std::string s) {
    set<char> chars;
    for (char c : string(s)) {
        chars.insert(c);
    }
    return chars.size();
}
