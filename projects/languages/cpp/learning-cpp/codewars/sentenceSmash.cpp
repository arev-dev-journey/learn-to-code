#include <iostream>
#include <vector>
#include <string>

using namespace std;

string smash(vector<string>& words)
{
  string sentence;
  for(size_t i = 0; i < words.size(); ++i)
  {
    sentence += words[i];
    if(i<words.size()-1)
    {
      sentence += " ";
    }
  }
  return sentence;
}
int main()
{

  vector<string> words = {"hello", "world"};
  cout << smash(words) << endl;
  return 0;
}
