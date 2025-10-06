#include <queue>
#include <list>
#include <iostream>
#include <stdio.h>

using namespace std;

void BFS(int G[][7], int start, int n)
{
  int i=start,j;
  int visited[7] {0};

  printf("%d ", i);
  visited[i]=1;
  enqueue(i);

  while(!isEmpty())
  {

    i=dequeue();
    for(j=1;j<n;++j)
    {
      if(G[i][j]==1 && visited[j]==0)
      {
        printf("%d, ", j);
        visited[j]=1;
        enqueue[j];
      }
    }
  }

}
int main()
{

  int G[7][7] = { {0,0,0,0,0,0,0},
                  {0,0,1,1,0,0,0},
                  {0,1,0,0,1,0,0},
                  {0,1,0,0,1,0,0},
                  {0,0,1,1,0,1,1},
                  {0,0,0,0,1,0,0},
                  {0,0,0,0,1,0,0}};
  return 0;
}
