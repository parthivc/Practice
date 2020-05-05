//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-11/o2uq6eTuvk7atGadR

std::string lineEncoding(std::string s) {
    string outputString = "";
    int index = 0, len = s.length();
    while (index < len) {
        char letter = s[index];
        int counter = 1;
        while (index < len && char(s[++index]) == letter) {
            counter++;
        }
        if (counter == 1) {
            outputString += letter;
        }
        else {
            outputString += to_string(counter) + letter;
        }
    }
    return outputString;
}
