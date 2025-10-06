#include <string>
#include <iostream>
#include <unordered_set>
#include <cctype>

bool is_isogram(const std::string& str)
{
    std::unordered_set<char> seen;
    for (char ch : str) {
        char lower_ch = std::tolower(ch); // Handle case-insensitivity
        if (seen.count(lower_ch)) {
            return false; // Duplicate character found
        }
        seen.insert(lower_ch);
    }
    return true; // No duplicates found
}

int main() {
    std::string str = "Dermatoglyphics"; // Example input
    std::cout << (is_isogram(str) ? "True" : "False") << std::endl;
}