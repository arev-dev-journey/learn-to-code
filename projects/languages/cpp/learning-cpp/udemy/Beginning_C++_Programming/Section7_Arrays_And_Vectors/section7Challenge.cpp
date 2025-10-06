/* Section 7 Challenge
 * Challenge
 *
 * Write a C++ program as follows:
 *
 * Declare 2 empty vectors of integers named vector1 and vector2 respectively.
 *
 * Add 10 and 20 to vector1 dynamically using push_back
 * Display the elements in vector1 using the at() method as well as its size using the size() method
 * Add 100 and 200 to vector2 dynamically using push_back
 * Display the elements in vector2 using the at() method as well as its size using the size() method
 *
 * Declare and empty 2D vector called vector_2d
 * Remember, that a 2D vector is a vector of vector<int>
 *
 * Add vector1 to vector_2d dynamically using push_back
 * Add vector2 to vector_2d dynamically using push_back
 * 
 * Display the elements in vector_2d using the at() method
 *
 * Change vector1.at(0) to 1000
 *
 * Display the elements in vector_2d again using the at() method
 *
 * Display the elements in vector1
 *
 * What did you expect? Did you get what you expected? What do you think happened?
 *
 */ 

#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int main() 
{
  vector<int> vector1, vector2;
  vector1.push_back(10);
  vector1.push_back(20);
  cout << "\nVector1 elements using vector syntax:" << endl;
  cout << vector1.at(0) << endl << vector1.at(1) << endl;
  cout << "\nThere are " << vector1.size() << " elements in the vector" << endl;

  vector2.push_back(100);
  vector2.push_back(200);
  cout << "\nVector2 elements using vector syntax:" << endl;
  printf("%d\n%d\n",vector2.at(0),vector2.at(1));
  printf("There are %lu elements in the vector\n", vector2.size());

  vector<vector<int>> vector_2d;
  vector_2d.push_back(vector1);
  vector_2d.push_back(vector2);
  cout << "\nVector_2d elements using vector syntax:" << endl;
  cout << vector_2d.at(0).at(0) << endl;
  cout << vector_2d.at(0).at(1) << endl;
  cout << vector_2d.at(1).at(0) << endl;
  cout << vector_2d.at(1).at(1) << endl;

  vector1.at(0) = 1000;
  cout << "\nVector_2d elements using vector syntax:" << endl;
  cout << vector_2d.at(0).at(0) << endl;
  cout << vector_2d.at(0).at(1) << endl;
  cout << vector_2d.at(1).at(0) << endl;
  cout << vector_2d.at(1).at(1) << endl;

  cout << "\nVector1 elements using vector syntax:" << endl;
  printf("%d\n%d\n", vector1.at(0),vector1.at(1));
  return 0;
}
