#include <stdio.h>
#include <iostream>

using namespace std;

void display(int *arr, int n)
{
 for(int i=0; i<n; ++i)
 {
   printf("%u ", arr[i]);
  printf("\n");
 }
}

int * fun(int size)
{
  int *p;
  p=new int[size];

  for(int i = 0; i < size; i++)
  p[i]=i+1;

  return p;
}

int main()
{
  int A[5];
  int n = 5;
  int B[5] {1,2,3,4,5};
  int C[10] {2,4,5};
  int D[5] {0};
  int E[] {1,2,3,4,5,6};

  display(A,n);
  display(B,n);
  display(C, n);
  display(D,n);
  display(E,n);

  int *ptr,sz=5;

  ptr=fun(sz);

  for(int i =0;i<sz;i++)
  cout << ptr[i] << endl;

  /* for(int i=0; i<sizeof(A)/sizeof(A[0]);++i) */
  /*   printf("%d, ", A[i]); */
  return 0;
}
