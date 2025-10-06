#include <string>
#include <iostream>

using namespace std;

string greet(const string &n)
{
  return "Hello, " + n + " how are you doing today?" ;
}

int main()
{
  cout << "Please enter your name" << endl;
  string name {};
  getline(cin, name);
  cout << greet(name) << endl;
}
