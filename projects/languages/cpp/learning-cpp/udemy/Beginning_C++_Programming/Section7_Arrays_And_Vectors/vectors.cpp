// Vectors
//
// Suppose we want to score test scores for my school
//
// What is a Vector?
// Container in the C++ Standard Template Lbin.usr-is-merged
//
// An array that can grow and shrink in size at execution time 
//
// Provides similar semantics and syntax as arrays
//
// Declaring
// #include <vector>
// using namespace std;
//
// vector<char> vowels;
// vector<int> test_scores;
//
// vector<char> vowels (5);
// vector<int> test_scores (10);
// 
// Initializing
//
// vector<char> vowels {'a', 'e', 'i', 'o', 'u'};
// vector<int> test_scores {100,98,89,85,93};
// vector<double> hi_temperatures (365, 80.0);
// Dynamic size, elements are all the same type, stored contiguously in memory, individual elements can be accessed by their position or index
// first element is at index 0 
// last element is at index.size-1
//
// [] - no checking to see if you are out of bounds
// provides many useful functions that do bounds check 
//
// elements initialized to zero 
// very efficient
// iteration (looping) is often used to process

// Vectors
// Accessing vector elements - array syntax
// vector_name [element_index]
//
// test_scores [1]
//

/*Playing with vectors, printing them out and playing with multi-dimensional vectors*/
/* #include <iostream> */
/* #include <vector> */
/* #include <stdio.h> */
/**/
/* using namespace std; */
/**/
/* int main() */
/* { */
/*   vector<vector<int>> test_scores {{100,100},{95,99},{87,88}}; */
/*   int i,n=3; */
/*   vector<int> test_scores0 = {100,95,99}; */
/**/
/*   for(i=0;i<n;i++) */
/*   printf("%d ", test_scores0[i]); */
/*   printf("\n"); */
/* } */

// Section 7
// Vectors

#include <iostream>
#include <vector>

using namespace std;

int main()
{
  // vector <char> vowels;      // empty
  // vector <char> vowels;      // 5 initialized to zero
  vector <char> vowels {'a','e','i','o','u'};

  cout << vowels[0] << endl;
  cout << vowels[4] << endl;

  // vector <int> test_scores(3); // 3 elements all initialized to zero
  // vector <int> test_scores(3,100); // 3 elements all initialized to 100
  //
  vector <int> test_scores {100,98,89};
  
  cout << "\nTest scores using array syntax:" << endl;
  cout << test_scores[0] << endl;
  cout << test_scores[1] << endl;
  cout << test_scores[2] << endl;
  cout << "\nThere are " << test_scores.size() << " scores in the vector" << endl;

  cout << "\nTest scores using the vector syntax:" << endl;

  cout << test_scores.at(0) << endl;
  cout << test_scores.at(1) << endl;
  cout << test_scores.at(2) << endl;
  cout << "\nThere are " << test_scores.size() << " scores in the vector" << endl;

  cout << "\nEnter 3 test scores: ";
  cin >> test_scores.at(0);
  cin >> test_scores.at(1);
  cin >> test_scores.at(2);

  cout << "\nUpdated test scores: " << endl;

  cout << test_scores.at(0) << endl << test_scores.at(1) << endl << test_scores.at(2) << endl;

  cout << "\nEnter a test score to add to the vector: ";

  int score_to_add {0};
  cin >> score_to_add;

  test_scores.push_back(score_to_add);

  cout << "\nEnter one or more test score to add to the vector: ";

  cin >> score_to_add;

  test_scores.push_back(score_to_add);

  cout << "\nTest scores are now: " << endl;

  cout << test_scores.at(0) << endl << test_scores.at(1) << endl << test_scores.at(2) << endl << test_scores.at(3) << endl << test_scores.at(4) << endl;
 
  cout << "\nThere are now " << test_scores.size() << " scores in the vector" << endl;

  // cout << "This should cause an exception!!" << test_scores.at(10);

  // Example of a 2D-vector
  //
   vector<vector<int>> movie_ratings
   {
   {1,2,3,4},
   {1,2,4,4},
   {1,3,4,5}
   };

  cout << "\nHere are the movie rating for reviewer #1 using array syntax:" << endl;
  cout << movie_ratings[0][0] << endl;
  cout << movie_ratings[0][1] << endl;
  cout << movie_ratings[0][2] << endl << movie_ratings[0][3] << endl;

  cout << "\nHere are the movie rating for reviewer #1 using vector syntax :" << endl;
  cout << movie_ratings.at(0).at(0) << endl << movie_ratings.at(0).at(1) << endl << movie_ratings.at(0).at(2) << endl << movie_ratings.at(0).at(3) << endl;
  
  cout << endl;
  for(int i=0;i<test_scores.size();i++)
  printf("%d ", test_scores[i]);
  printf("\n");

  return 0;
}
