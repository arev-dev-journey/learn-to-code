#include <iostream>
#include <stdio.h>

using namespace std;

class Rectangle
{
public:
  int length;
  int width;

void initialize(int l, int w)
{
  length=l;
  width=w;
}

int area()
{
  return length * width;
}

int perimeter()
{
  int p;
  p = 2*(length+width);
  return p;
}

};
int main() 
{

  Rectangle r = {0,0};
  int l,w;
  printf("Enter Length and Width");
  cin>>l>>w;

  r.initialize(l, w);

  int a = r.area();
  int p = r.perimeter();

  printf("Area is %d\nPerimeter is %d\n", a, p);

  return 0;
}
