#include <iostream>
using namespace std; 

int main() {
    std::cout << "Hello, World!" << std::endl;
    
    int num1;
    int num2;
    double num3;

    cout << "Enter an integer";
    cin >> num1;
    cout << "You entered: " << num1 << endl;
    
    cout << "Enter a first integer: ";
    cin >> num1;

    cout << "Enter a second integer: ";
    cin >> num2;

    cout << "You entered " << num1 << " and " << num2 << endl;

    cout << "Enter 2 numbers separated with a space: ";
    cin >> num1 >> num2;
    cout << "You entered " << num1 << " and " << num2 << endl;

    cout << "Enter a double: ";
    cin >> num3;

    cout << "You entered: " << num3 << endl;

    cout << "Enter an integer: ";
    cin >> num1;

    cout << "Enter a double: ";
    cin >> num3;

    cout << "The integer is: " << num1 << endl;
    cout << "And the double is: " << num3 << endl;

    return 0;

  }
