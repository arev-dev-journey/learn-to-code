package leetcode.google;

public class BinarySearchAlgorithm {

  public int binarySearch(int[] intArray, int target) {
    int low = 0;
    int high = intArray.length - 1;

    while (low <= high) {
      int mid = low + (high - low) / 2;

      if (intArray[mid] == target) {
        return mid;
      } else if (intArray[mid] < target) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return -1;
  }

  public static void main(String[] args) {
    BinarySearchAlgorithm searchAlgorithm = new BinarySearchAlgorithm();

    int sortedArray[] = { 1, 3, 5, 7, 9, 11, 13, 15 };
    int target = 9;

    int result = searchAlgorithm.binarySearch(sortedArray, target);

    if (result != -1) {
      System.out.println("Target " + target + " found at index: " + result);
    } else {
      System.out.println("Target " + target + "not found.");
    }

  }
}
