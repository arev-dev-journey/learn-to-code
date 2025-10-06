#include <iostream>
#include <set>

using namespace std;

class Person
{
  friend ostream &operator<<(ostream &os, const Person &p);
  string name;
  int age;
public:
  Person() : name{"Unknown"},age{0} {}
  Person(string name, int age)
    : name{name}, age{age} {}
  bool operator<(const Person &rhs) const {
    return this->age < rhs.age;
  }
  bool operator==(const Person &rhs) const{
    return (this->name == rhs.name && this-> age == rhs.age);
  }
};

ostream &operator << (ostream &os, const Person &p)
{
  os << p.name << ":" << p.age;
  return os;
}

template <typename T>
void display(const set<T> &l)
{
  cout << "[";
  for (const auto &elem : l)
  {
    cout << elem << " ";
  }
  cout << "]" << endl;
}


int main()
{
  set<int> s1 {1,4,3,5,2};
  display(s1);

  return 0;
}
