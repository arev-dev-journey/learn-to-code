#include <iostream>
#include <stdio.h>
#include <string>
#include <cstring>

using namespace std;

struct Rectangle
{
  int length;
  int breadth;
  char x;
} r1, r2, r3;

struct Card
{
  int face;
  int shape;
  int color;
};

struct Student {
int roll;
string name;
char dept[10];
char address[50];
};

int main() {

  struct Rectangle r4={10,5};   // initializing structure


  printf("%lu\n", sizeof(r4));

  r4.length=15;
  r4.breadth=7;

  cout<<r4.length<<endl;
  cout<<r4.breadth<<endl;
  struct Student s;
  s.roll = 10;
  s.name = "Alex";

  struct Card deck[52] = {{1,0,0},{2,0,0},{1,1,0},{2,1,0}};

  printf("%d\n",deck[0].face);
  printf("%d\n",deck[0].shape);

  printf("Student roll is %d and student name is %s\n", s.roll, s.name.c_str());

  return 0;
}
