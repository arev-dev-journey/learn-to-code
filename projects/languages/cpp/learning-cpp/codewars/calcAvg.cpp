#include <vector>
#include <iostream>

double calcAverage(std::vector<int>& values)
{
  double sum = 0.0;
  for(auto i : values)
    sum += i;
  return sum / values.size();
}

int main()
{
  std::vector<int> values {100,32,55,20,122};
  std::cout << calcAverage(values) << std::endl;
}
