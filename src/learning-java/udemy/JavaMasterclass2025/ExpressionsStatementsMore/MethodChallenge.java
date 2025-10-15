public class MethodChallenge {

  public static void displayHighScorePosition(String playerName, int highScorePosition) {
    System.out.println(playerName + " managed to get into position " + highScorePosition + " on the high score list");

}

  public static int calculateHighScorePosition(int playerScore) {
    int position = 4;

    if (playerScore >= 1000) {
      position = 1;
    } else if (playerScore >= 500) {
      position = 2;
    } else if (playerScore >= 100) {
      position = 3;
    } 
    return position;
  }

  public static void main(String[] args) {
    displayHighScorePosition("Alex", calculateHighScorePosition(1500));
    displayHighScorePosition("Tim", calculateHighScorePosition(1000));
    displayHighScorePosition("Vanessa", calculateHighScorePosition(500));
    displayHighScorePosition("David", calculateHighScorePosition(100));
    displayHighScorePosition("Angelique", calculateHighScorePosition(25));
  }
}
