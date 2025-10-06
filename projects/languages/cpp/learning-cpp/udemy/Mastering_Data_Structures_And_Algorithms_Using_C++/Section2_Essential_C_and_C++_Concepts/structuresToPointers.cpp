#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

struct Rectangle 
{
  int length;
  int width;

};

int main() 
  {
    /* Rectangle r = {10,5}; */
    /* cout<<r.length<<endl; */
    /* cout<<r.width<<endl; */
    /**/
    /* Rectangle *p=&r; */
    /* cout<<p->length<<endl; */
    /* cout<<p->width<<endl; */
    
    // To create an object of Rectangle in Heap
    Rectangle *p;
    // p=(struct Rectangle *)malloc(sizeof(struct Rectangle)); // c lang
    p=new Rectangle;    // in c++ lang

    p->length=15;
    p->width=7;

    cout<<p->length<<endl;
    cout<<p->width<<endl;

    return 0;
  }
