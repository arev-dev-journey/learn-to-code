/* Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return
 * the number of islands.
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 * You may assume all four edges of the grid are all surrounded by water.
 */

/*
 * Example 1:
 * Input: grid = [
 * ["1","1","1","1","0"],
 * ["1","1","0","1","0"],
 * ["1","1","0","0","0"],
 * ["0","0","0","0","0"]
 * ]
 * Output: 1
 * Constraints: m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 300
 * grid[i][j] is '0' or '1'
 */

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
private: 
  int m, n;
public:
  vector<vector<int>> dirs = {{0,1},{1,0},{0,-1},{-1,0}};
  
  void dfs(vector<vector<char>>& grid, int r, int c)
  {
    for(vector<int> dir : dirs)
      {
        int nr = r + dir[0];
        int nc = c + dir[1];

        if (0 <= nr && nr < m && 0 <= nc && nc < n && grid[nr][nc] == '1')
        {
          grid[nr][nc] = '0';
          dfs(grid, nr, nc);
        }
      }
  }
  int numIslands(vector<vector<char>>& grid)
  {
    m = grid.size();
    n = grid[0].size();
    int count = 0;

    for (int r = 0; r < m; r++)
    {
      for (int c = 0; c < n; c++)
      {
        if (grid[r][c] == '1')
        {
          count++;
          dfs(grid,r,c);
        }
      }
    }
    return count;
  }
};

int main()
{
  vector<vector<char>> grid {
    {'1','1','1','1'},
    {'1','1','0','1'},
    {'1','1','0','0'},
    {'1','1','0','0'},
    {'0','0','0','0'}
  };

  vector<vector<char>> grid2 {
    {'1','1','0','0','0'},
    {'1','1','0','0','0'},
    {'0','0','1','0','0'},
    {'0','0','0','1','1'}
  };
  Solution solution;
  cout << solution.numIslands(grid2) << endl;
  return 0;
}
