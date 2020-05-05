//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-10/TXFLopNcCNbJLQivP

std::string findEmailDomain(std::string address) {
    return address.substr(address.find_last_of("@") + 1);
}
