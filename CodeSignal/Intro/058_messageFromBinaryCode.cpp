//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-12/sCpwzJCyBy2tDSxKW

std::string messageFromBinaryCode(std::string code) {
    string message = "";
    for (int index = 0; index < code.length() / 8; index++) {
        char parsed = 0;
        for (int i = 0; i < 8; i++) {
            if (code[index * 8 + i] == '1') {
                parsed |= 1 << (7 - i);
            }
        }
        message += parsed;
    }
    return message;
}
