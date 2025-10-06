#include <iostream>

using namespace std;

// in this function we are returning an array of integers and 
// passing the desired size of the array as a parameter
int * fun(int size)
{
  int *p;   // create a pointer of type integer, p
  p = new int[size];    // initialize pointer into heap memory

  for(int i =0; i < size; i++)  // create for loop to loop through array and assign value of i + 1, until desired size is reached
  p[i]= i+1;

  return p; // return array 
}

//void fun(int *A, int n) 
//{
  /* cout << sizeof(A)/sizeof(int) << endl; */
  /* for(int i = 0;i<5;i++) */
  /* cout << A[i] << endl; */
  /**/

  // A[0]=15;
//}

int main() 
{
  /* int A[] = {2,4,6,8,10}; */
  /* int n = 5; */
  /* fun(A,n); */
  /*  cout<<sizeof(A)/sizeof(int) << endl; */ 
  /* for(int x : A) */
  /* cout << x << " "; */
  /**/

  int *ptr, sz=7;   // initialize array of integer pointers, ptr and size, 7

  ptr=fun(sz);  // call function fun, passing 7 as size and assign to integer array ptr

  for(int i = 0; i < sz; i++)   // for loop printing out each index of created array ptr
  cout << ptr[i] << endl;

  return 0;
}
