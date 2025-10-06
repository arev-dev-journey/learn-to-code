
public class OverloadedChallenge {
  public static void main(String[] args) {
    System.out.println("75 inches = " + convertToCentimeters(75) + " cm");
    convertToCentimeters(6,3);
}
 public static double convertToCentimeters(int inches) {
    return inches * 2.54;
}

public static double convertToCentimeters(int feet, int inches) {
    int totalInches = (feet * 12) + inches;
    double result = convertToCentimeters(totalInches);
    System.out.println(feet + " feet, " + inches + " inches = " + result + " cm");
    return result;
    
}
}
