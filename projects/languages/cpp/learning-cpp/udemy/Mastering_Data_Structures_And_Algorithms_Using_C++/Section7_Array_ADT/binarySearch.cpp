#include <stdio.h>
using namespace std;

struct Array
{
  int A[20];
  int length,size;
};


void Display(struct Array arr)
{
  printf("\nEnter the elements of the array\n");
  for(int i=0;i<arr.length;i++)
    printf("%d ",arr.A[i]);
  printf("\n");
}

// Iterative version
int BinarySearch(struct Array arr, int key)
{
  int l,mid,h;
  l=0;
  h=arr.length-1;

  while(l<=h)
    {
      mid=(l+h)/2;
      if(key==arr.A[mid])
        return mid;
      else if(key<arr.A[mid])
        h=mid-1;
      else {
        l=mid+1;
      }
    }
  return -1;
}

// Recursive BinarySearch
int RBinSearch(int a[], int l, int h, int key)
{
  int mid;

  if(l<=h)
  {
    mid=(l+h)/2;
    if(key==a[mid])
      return mid;
    else if(key<a[mid])
      return RBinSearch(a,l,mid-1,key);
    else
      return RBinSearch(a,mid+1,h,key);
  }
  return -1;
}

int main()
{

  struct Array arr {{2,3,4,5,6},10,5};
  
  printf("%d\n",RBinSearch(arr.A,0,arr.length,5));
  printf("%d\n",BinarySearch(arr,5));
  Display(arr);


  return 0;
}
