#include <stdio.h>
#include <iostream>

using namespace std;

struct Array
{
  int A[20];
  int length,size;

};

void swap(int *x, int *y)
{
  int temp = *x;
  *x = *y;
  *y = temp;
}

void Display(struct Array arr)
{
  int i;
  printf("\nElements are\n");
  for(i=0;i<arr.length;++i)
    printf("%d ",arr.A[i]);
}

int LinearSearch(struct Array *arr, int key)
{
  int i;
  for(i=0;i<arr->length;i++)
  {
    if(key==arr->A[i])
    {
      swap(&arr->A[i],&arr->A[i-1]);
      return i;
    }
  }
  return -1;
}

int main()
{

  struct Array arr={{2,3,4,5,6},10,5};

  printf("%d\n",LinearSearch(&arr,5));
  Display(arr);

  return 0;
}
