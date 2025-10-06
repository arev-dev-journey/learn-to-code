#include <iostream>
#include <vector>
using namespace std;

int main()
{
  // foreach loop = loop that eases the traversal over an iterable data set
  //

  //std::string students[] = {"Spongebob", "Patrick", "Squidward"};

  vector<int> grades {65, 72, 81, 93};
  
  for(int grade : grades)
  {
    cout << grade << endl;
  }
  
  return 0;
}
