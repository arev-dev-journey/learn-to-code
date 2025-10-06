#include <iostream>
#include <stdio.h>

using namespace std;

int main() 
{
  int length=0, width=0;

  printf("Enter Length and Width");
  cin >> length >> width;

  int area = length * width;

  int perimeter = 2 * (length + width);

  printf("Area = %d\nPerimeter = %d\n", area, perimeter);

  return 0;
}
