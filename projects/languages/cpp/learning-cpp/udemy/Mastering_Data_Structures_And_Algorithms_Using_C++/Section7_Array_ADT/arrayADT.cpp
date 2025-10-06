// Operations on Array
#include <iostream>
#include <stdio.h>

using namespace std;

struct Array
{
  int A[20];
  int size,length;
};

void Display(struct Array arr)
{
  int i;
  printf("\nElements are\n");
  for(i=0;i<arr.length;++i)
    printf("%d ",arr.A[i]);
}

void Append(struct Array *arr, int x)
{
  if(arr->length<arr->size)
    arr->A[arr->length++]=x;
}

void Insert(struct Array *arr, int index, int x)
{
  if(index >=0 && index <= arr->length)
  {
    for(int i=arr->length;i>index;i--)
      arr->A[i]=arr->A[i-1];
    arr->A[index]=x;
    arr->length++;
  }
}

int Delete(struct Array *arr, int index)
{
  int x=0;
  int i;

  if(index>=0 && index < arr->length)
  {
    x=arr->A[index];
    for(i=index;i<arr->length-1;i++)
      arr->A[i]=arr->A[i+1];
    arr->length--;
    return x;
    
  }
  return 0;
}
int main()
{
  struct Array arr {{2,3,4,5,6},10,5};

  printf("%d\n",Delete(&arr,0));
    Display(arr);

  //Insert(&arr, -1,10);
  //Append(&arr,9);
  /* int n,i; */
  /* printf("Enter the size of the array\n"); */
  /* scanf("%d", &arr.size); */
  /* arr.A=(int *)malloc(arr.size*sizeof(int)); */
  /* arr.length=0; */
  /**/
  /* printf("Enter number of numbers\n"); */
  /* scanf("%d",&n); */
  /**/
  /* printf("Enter all Elements\n"); */
  /* for(i=0;i<n;++i) */
  /*   scanf("%d",&arr.A[i]); */
  /* arr.length=n; */
  /**/

  return 0;
}

