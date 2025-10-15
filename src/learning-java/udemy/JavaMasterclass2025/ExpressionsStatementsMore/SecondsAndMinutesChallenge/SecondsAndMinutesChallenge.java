public class SecondsAndMinutesChallenge {
  public static String getDurationString(int seconds) {

  if (seconds < 0) {
      return "Invalid Value";
    } else {
      int hours = seconds / 3600;
      int minutes = (seconds % 3600) / 60;
      int remSeconds = (seconds % 3600) % 60;
      return hours + "h " + minutes + "m " + remSeconds + "s ";
    }
  }

  public static String getDurationString(int minutes, int seconds) {
    if (minutes < 0 || seconds < 0) {
    return "Invalid Value";
    } else {
      int hours = minutes / 60;
      int totalMinutes = (minutes % 60) + seconds/60;
      int remSeconds = (seconds % 3600) % 60;
      return hours + "h " + totalMinutes + "m " + remSeconds + "s ";
    }
  }
  public static void main(String[] args) {
    String result = getDurationString(-1);
    String test1 = getDurationString(3945); // 1h 5m 45s
    String test2 = getDurationString(360, 345); // 360m and 345s = 6 h 5m 45s
    System.out.println(result);
    System.out.println(test1);
    System.out.println(test2);
  }
}
