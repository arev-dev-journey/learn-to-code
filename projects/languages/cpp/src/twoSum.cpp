/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 */

#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution{
public:
  static vector<int> twoSum(vector<int> nums, int target)
  {
    for(int i = 0; i<nums.size(); ++i)
    {
      for(int j = i+1; j<nums.size(); ++j)
        if(nums[i] == target - nums[j])
        {
          return {i,j};
        }
    }
    return {}; // no solution found
  }
  
  static vector<int> onePassTwoSum(vector<int> &nums, int target)
  {
    unordered_map<int, int> hash;
    for(int i =0; i<nums.size(); ++i)
    {
      int complement = target - nums[i];
      if(hash.find(complement) != hash.end())
      {
        return {hash[complement],i};
      }
      hash[nums[i]] = i;
    }
    return {};
  }
};

int main()
{

  vector<int> nums {3,3};
  vector<int> nums1 {12,17,7,2};
  int target2 = 9;
  int target = 6;

  vector<int> result1 = Solution::twoSum(nums1, target2);
  vector<int> result2 = Solution::onePassTwoSum(nums,target);

  cout << "Result 1: " << result1[0] << " and " << result1[1] << endl;
  cout << "Result 2: " << result2[0] << " and " << result2[1] << endl;


  return 0;
}
