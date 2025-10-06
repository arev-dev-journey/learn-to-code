#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;



int main()
{

  // create array inside stack
  int A[3][4] {{1,2,3,4}, {2,4,6,8}, {1,3,5,7}};

  int *B[3];
  int **C;
  int i,j;

  for(i=0; i<3; ++i)
  {
    for(j=0;i<4;++j)
    {
      printf("%d ", A[i][j]);
    printf("\n");
    }
  }

  B[0]=(int *)malloc(4*sizeof(int));
  B[1]=(int *)malloc(4*sizeof(int));
  B[2]=(int *)malloc(4*sizeof(int));

  C=(int **)malloc(3*sizeof(int *));
  C[0]=(int *)malloc(4*sizeof(int));
  C[1]=(int *)malloc(4*sizeof(int));
  C[2]=(int *)malloc(4*sizeof(int));
  C[3]=(int *)malloc(4*sizeof(int));

  return 0;

} 
