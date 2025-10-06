#include <iostream>

using namespace std;

struct Rectangle
{
  int length;
  int width;
};
// return a pointer of type Rectangle, create object of Rectangle on Heap
struct Rectangle *fun()
{
  struct Rectangle *p;
  p=new Rectangle;

  p->length=15;
  p->width=7;

  return p;
}

/* void fun(struct Rectangle *p)   // pointer of type Rectangle */
/* { */
/*   p->length = 20; */
/*   cout << "Length " << p->length << endl << "Width "  << p->width << endl; */
/* } */
/**/

int main()
{
  struct Rectangle *ptr = fun();

  cout << "Length " << ptr->length << endl << "Width " << ptr->width << endl;
  /* Rectangle r = {10, 5}; */
  /* fun(&r); */
  /**/
  /* printf("Length %d \nWidth %d \n",r.length, r.width); */
  /* return 0; */
  return 0;
}
