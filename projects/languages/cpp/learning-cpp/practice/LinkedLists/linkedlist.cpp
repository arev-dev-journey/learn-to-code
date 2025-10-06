#include <iostream>
using namespace std;

class Node
{
public:
  int data;     // Stores the data
  Node* next;   // Pointer to the next node

  // Constructor to initialize a node
  Node(int value)
  {
    data = value;
    next = nullptr;     // Initially, the next pointer is NULL
  }
  

};

// Linked List class
class LinkedList 
{
private:
  Node* head;   // Pointer to the first node

public:
  // Constructor: Initializes an empty list
  LinkedList()
  {
    head = nullptr;
  }

  // Destructor: Free memory when object is destroyed
  ~LinkedList()
  {
    Node* temp;
    while(head!=nullptr)
    {
      temp = head;
      head = head->next;
      delete temp;
    }
  }

  // Insert at the end of the list
  void insert(int value)
    {
      Node* newNode = new Node(value);     // Create a new node

      if(head == nullptr)   // If the list is empty
      {
        head = newNode;
        return;
      }

      // Traverse to the last node
      Node* temp = head;
      while(temp->next != nullptr)
      {
        temp=temp->next;
      }

      temp->next = newNode;     // Link the last node to the new node
    }

  // Insert at the beginning of the list
  void insertBeginning(int value)
  {
    Node* newNode = new Node(value);
    newNode->next = head;
    head = newNode;
  }

  // Insert at a specific position (0-based index)
  void insertAt(int value, int position)
  {
    if(position == 0)
    {
      insertBeginning(value);
      return;
    }

    Node* newNode = new Node(value);
    Node* temp = head;

    // Traverse to the postion before the insertion point
    for(int i = 0; temp!=nullptr && i < position-1; i++)
    {
      temp = temp->next;
    }

    if(temp==nullptr)
    {
      cout << "Position out of range" << endl;
      return;
    }

    newNode->next = temp->next;
    temp->next = newNode;
}

  // Delete a node by value
  void deleteByValue(int value)
{
  if(head==nullptr)
  {
    cout << "List is empty!" << endl;
    return;
  }

  if(head->data==value)
  {
    Node* temp = head;
    head = head->next;
    delete temp;
    return;
  }

  Node* temp = head;
  while(temp->next != nullptr && temp->next->data != value)
  {
    temp = temp->next;
  }

  if(temp->next == nullptr)
  {
    cout << "Value not found in list!" << endl;
    return;
  }


  Node* toDelete = temp->next;
  temp->next = temp->next->next;
  delete toDelete;
}
  
  // Search for a value
  bool search(int value)
{
  Node* temp = head;
  while(temp != nullptr)
  {
    if(temp->data == value)
    {
      return true;
    }
    temp = temp->next;
  }
  return false;
}

  // Reverse the linked list iteratively
  void reverseIterative()
{
  Node* prev = nullptr;
  Node* current = head;
  Node* next = nullptr;

  while(current != nullptr)
  {
    next = current->next;   // Store next node
    current->next = prev;   // Reverse the link
    prev = current;         // Move prev to current 
    current = next;         // Move current to next
  }
  head = prev;  // Update head to the new first node
}

Node* reverseRecursive(Node* node)
{
  if(node == nullptr || node->next == nullptr)
  {
    return node;
  }

  Node* newHead = reverseRecursive(node->next); // Reverse rest
  node->next->next = node;  // Make next node point back to the current
  node->next = nullptr; // Set current node's next to NULL

  return newHead;   // Return new head node
}

void reverseRecursiveWrapper()
{
  head = reverseRecursive(head);
} 

  // Display the linked list
  void display()
  {
    Node* temp = head;
    while(temp != nullptr)
    {
      cout << temp->data << " -> ";
      temp = temp->next;
    }
    cout << "NULL" << endl;
  }

};

int main()
{
  cout << "Hello, Alex. Let's learn LinkedLists" << endl;
  LinkedList list;

  list.insert(10);
  list.insert(20);
  list.insert(30);

  cout << "Linked List: ";
  list.display();

  list.insertBeginning(5);
  cout << "After inserting at beginning: " << endl;
  list.display();

  list.insertAt(15,2);      // Insert 15 at index 2
  cout << "After inserting at position 2: " << endl;
  list.display();

  list.deleteByValue(20);
  cout << "After deleting 20: ";
  list.display();

  int searchValue = 15;
  if(list.search(searchValue))
  {
    cout << searchValue << " found in the list" << endl;
  } else {
    cout << searchValue << " not found in the list" << endl;
  }

  list.reverseIterative();
  cout << "Reversed List (Iterative): ";
  list.display();

  list.reverseRecursiveWrapper();
  cout << "Reversed List (Recursive): ";
  list.display();

  return 0;
}
