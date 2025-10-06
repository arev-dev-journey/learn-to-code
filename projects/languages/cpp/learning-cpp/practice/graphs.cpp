#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class AdjListGraph
{
public:
  unordered_map<int, vector<int>> adjList;      // Adjacency List Representation

  void addEdge(int u, int v, bool directed)
  {
    adjList[u].push_back(v);
    if(!directed)
      adjList[v].push_back(u);  // If undirected, add both directions
  }

  void printGraph()
  {
    for(auto& pair : adjList)
    {
      cout << pair.first << " -> ";
      for(int neighbor : pair.second)
      {
        cout << neighbor << " ";
      }
      cout << endl;
    }
  }
};

class AdjMatGraph
{
public:
  vector<vector<int>> adjMatrix;
  int V;

  AdjMatGraph(int vertices)
  {
    V = vertices;
    adjMatrix.resize(V, vector<int>(V, 0));
  }

  void addMatEdge(int u, int v, bool directed)
  {
    adjMatrix[u][v] = 1;
    if(!directed)
      adjMatrix[v][u] = 1;
  }

  void printMatGraph()
  {
    for(int i = 0; i < V; i++)
    {
      for(int j = 0; j < V; j++)
      {
        cout << adjMatrix[i][j] << " ";
      }
      cout << endl;
    }
  }

};

int main()
{
  AdjListGraph g;
  g.addEdge(1,2,false);
  g.addEdge(1,3, false);
  g.addEdge(2,4,false);
  g.addEdge(3,5,false);

  g.printGraph();

  AdjMatGraph mg(4);
  mg.addMatEdge(0,1,false);
  mg.addMatEdge(0,2,false);
  mg.addMatEdge(1,3,false);

  mg.printMatGraph();
  return 0;
}
