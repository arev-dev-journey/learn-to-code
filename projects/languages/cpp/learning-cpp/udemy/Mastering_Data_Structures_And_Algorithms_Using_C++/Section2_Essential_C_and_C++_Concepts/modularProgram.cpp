#include <iostream>
#include <stdio.h>

using namespace std;

int area(int length, int width)
{
  return length * width;
}

int perimeter(int length, int width)
{
  int p;
  p = 2*(length+width);
  return p;
}

int main() 
{
  int length=0, width=0;

  printf("Enter Length and Width");
  cin>>length>>width;

  int a = area(length, width);
  int p = perimeter(length, width);

  printf("Area is %d\nPerimeter is %d\n", a, p);

  return 0;
}
