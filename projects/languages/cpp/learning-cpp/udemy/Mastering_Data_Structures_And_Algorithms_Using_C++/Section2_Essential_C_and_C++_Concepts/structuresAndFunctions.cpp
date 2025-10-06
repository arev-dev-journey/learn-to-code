#include <iostream>
#include <stdio.h>

using namespace std;

struct Rectangle
{
  int length;
  int width;
};

void initialize(struct Rectangle *r, int l, int w)
{
  r->length=l;
  r->width=w;
}

int area(struct Rectangle r)
{
  return r.length * r.width;
}

int perimeter(struct Rectangle r)
{
  int p;
  p = 2*(r.length+r.width);
  return p;
}

int main() 
{

  Rectangle r = {0,0};
  int l,w;
  printf("Enter Length and Width");
  cin>>l>>w;

  initialize(&r, l, w);
  int a = area(r);
  int p = perimeter(r);

  printf("Area is %d\nPerimeter is %d\n", a, p);

  return 0;
}
