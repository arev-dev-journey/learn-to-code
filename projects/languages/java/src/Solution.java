class Solution {

  public static int solution(int[] A) {
    int moves = A[0];
    int n = A.length;

    for (int i = 1; i < n; i++) {
      if (A[i] > A[i - 1]) {
        moves += A[i] - A[i - 1];
      }
    }
    return moves;
  }
}
