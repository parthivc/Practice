//
// Created by Parthiv Chigurupati on 5/5/20.
//

// Problem Statement: https://app.codesignal.com/arcade/intro/level-10/ppZ9zSufpjyzAsSEx

bool isPalindrome(string &str) {
    return str.length() >= 3 && str == string(str.rbegin(), str.rend());
}

std::string buildPalindrome(std::string st) {
    if (isPalindrome(st)) {
        return st;
    }
    int index = 1;
    string palindrome = "", postFix;
    while (!isPalindrome(palindrome)) {
        postFix = st.substr(0, index++);
        postFix = string(postFix.rbegin(), postFix.rend());
        palindrome = st + postFix;
    }
    return palindrome;
}
