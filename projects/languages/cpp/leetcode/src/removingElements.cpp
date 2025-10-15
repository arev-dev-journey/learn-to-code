#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

class Solution {
public:
  int removeElements(vector<int>& nums, int val) {
    int count = 0;
    for(int i = 0; i < nums.size(); ++i) {
      if(nums[i] != val) {
        nums[count] = nums[i];
        count++;
      }
    }
    return count;
  }
};

int main() {
  vector<int> nums {0,1,2,2,3,0,4,2};
  int target = 2;

  Solution s;
  cout << s.removeElements(nums, target);
  cout << endl;

  int newSize = s.removeElements(nums, target);

  cout << "Modified Array: ";
  for(int i = 0; i < newSize; ++i)
    cout << nums[i] << " ";
  cout << endl;

  return 0;
}
