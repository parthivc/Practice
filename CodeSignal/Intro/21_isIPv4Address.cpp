//
// Created by Parthiv Chigurupati on 5/4/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso

bool isIPv4Address(std::string inputString) {
    stringstream checker(inputString);
    string element;
    int counter = 0;
    int val;
    try {
        while (getline(checker, element, '.')) {
            val = stoi(element);
            if (element.empty() || ++counter > 4 || element != to_string(val) || 255 < val || val < 0) {
                return false;
            }
        }
        return counter == 4;
    }
    catch(...) {
        return false;
    }

}
