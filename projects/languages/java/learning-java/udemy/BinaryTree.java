import java.util.Stack;

public class BinaryTree {
  private TreeNode root;

  private class TreeNode {
    private TreeNode left;
    private TreeNode right;
    private int data; // Generic type

    public TreeNode(int data) {
      this.data = data;
    }
  }

  public void createBinaryTree() {
    TreeNode first = new TreeNode(9);
    TreeNode second = new TreeNode(2);
    TreeNode third = new TreeNode(3);
    TreeNode fourth = new TreeNode(4);
    // TreeNode fifth = new TreeNode(5);

    root = first; // root ---> first
    first.left = second;
    first.right = third; // second <--- first ---> third

    second.left = fourth;
    // second.right = fifth;

  }

  // Recursive preOrder Traversal
  // public void preOrder(TreeNode root) {
  // if (root == null) {
  // return;
  // }
  // System.out.println(root.data);
  // preOrder(root.left);
  // preOrder(root.right);
  // }

  // Iterative preOrder Traversal Method
  public void preOrder(TreeNode root) {
    if (root == null) {
      return;
    }

    Stack<TreeNode> stack = new Stack<>();
    stack.push(root);

    while (!stack.isEmpty()) {
      TreeNode temp = stack.pop();
      System.out.println(temp.data);
      if (temp.right != null) {
        stack.push(temp.right);
      }
      if (temp.left != null) {
        stack.push(temp.left);
      }
    }
  }

  // Recursive inOrder binary tree traversal
  // public void inOrder(TreeNode root) {
  // if (root == null) {
  // return;
  // }
  // inOrder(root.left);
  // System.out.println(root.data);
  // inOrder(root.right);
  // }

  // Iterative inOrder binary tree Traversal
  public void inOrder(TreeNode root) {
    if (root == null) {
      return;
    }

    Stack<TreeNode> stack = new Stack<>();
    TreeNode temp = root;
    while (!stack.isEmpty() || temp != null) {
      if (temp != null) {
        stack.push(temp);
        temp = temp.left;
      } else {
        temp = stack.pop();
        System.out.println(temp.data);
        temp = temp.right;
      }
    }
  }

  public static void main(String[] args) {
    BinaryTree bt = new BinaryTree();
    bt.createBinaryTree();
    // bt.preOrder(bt.root);
    bt.inOrder(bt.root);

  }
}
