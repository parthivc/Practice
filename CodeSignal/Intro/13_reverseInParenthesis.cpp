//
// Created by Parthiv Chigurupati on 5/3/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6

std::string reverseInParentheses(std::string inputString) {
    std::string output = "";
    stack<char> s;
    for (char letter : inputString) {
        if (letter == ')') {
            std::string tmp = "";
            while (!s.empty()) {
                char c = s.top();
                s.pop();
                if (c == '(') {
                    break;
                }
                tmp += c;
            }
            for (char letter : tmp) {
                s.push(letter);
                cout << letter << endl;
            }
        }
        else {
            s.push(letter);
        }
    }
    while (!s.empty()) {
        output += s.top();
        s.pop();
    }
    reverse(output.begin(), output.end());
    return output;
}
