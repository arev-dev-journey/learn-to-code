#include <iostream>
#include <climits>
using namespace std;

struct TreeNode
{
  int val;  // Value stored in the node
  TreeNode* left; // Pointer to the left child
  TreeNode* right; // Pointer to the right child

  TreeNode(int x) : val(x), left(NULL), right(NULL) {}  // Constructor
};

// Implement basic traversal
// PREORDER traversal
void preorder(TreeNode* root)
{
  if(root!=NULL)
  {
    cout << root->val << " ";   // Visit root
    preorder(root->left);       // Visit the left node
    preorder(root->right);      // Visit the right node
  }
}
// INORDER traversal
void inorder(TreeNode* root)
{
  if(root!=NULL)
  {
    inorder(root->left);        // Visit the left node
    cout << root->val << " ";   // Visit root
    inorder(root->right);       // Visit the right node;
  }
}
// POSTORDER traversal
void postorder(TreeNode* root)
{
  if(root!=NULL)
  {
    postorder(root->left);      // Visit the left node
    postorder(root->right);     // Visit the right node
    cout << root->val << " ";   // Visit root
  }
}

void mirrorTree(TreeNode* root)
{
  if(root!=NULL)
  {
    swap(root->left, root->right);
    mirrorTree(root->left);
    mirrorTree(root->right);
  }
}

bool isBSTHelper(TreeNode* root, long minVal, long maxVal)
{
  if(root==NULL)
    return true;    // Base case: An empty tree is a BST
  if(root->val <= minVal || root->val >= maxVal)
    return false;   // If value is out of range of BST, it's not a BST

  return isBSTHelper(root->left, minVal, root->val) &&  // left subtree must be < root
    isBSTHelper(root->right, root->val, maxVal);        // right subtree must be > than root
}

bool isValidBST(TreeNode* root)
{
  return isBSTHelper(root, LONG_MIN, LONG_MAX);
}
  int main()
{

  cout << "Hello, Alex, let's learn trees" << endl;

  // Creating the tree structure
  TreeNode* root = new TreeNode(8);
  root->left = new TreeNode(4);
  root->right = new TreeNode(10);
  root->left->left = new TreeNode(7);
  root->left->right = new TreeNode(6);
  root->right->right = new TreeNode(20);

  // Check if is isValidBST
  cout << (isValidBST(root) ? "Valid BST" : "Invalid BST") << endl;

  // Running Traversals
  cout << "Preorder Traversal: ";
  preorder(root);
  cout << "\n";

  cout << "Inorder Traversal: ";
  inorder(root);
  cout << "\n";

  cout << "Postorder Traversal: ";
  postorder(root);
  cout << "\n";

  mirrorTree(root);
  cout << "Inorder after mirroring: ";
  inorder(root);
  cout << "\n";

  return EXIT_SUCCESS;
}
