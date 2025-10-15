/**
 * Loop Practice Exercises
 * Various loop implementations for practice
 */
public class LoopPractice {
    public static void main(String[] args) {
        System.out.println("=== For Loop Examples ===");
        
        // Count from 1 to 10
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        // Count down from 10 to 1
        for (int i = 10; i >= 1; i--) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        // Print even numbers
        for (int i = 2; i <= 20; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        System.out.println("\n=== While Loop Examples ===");
        
        // Factorial calculation
        int number = 5;
        int factorial = 1;
        int temp = number;
        
        while (temp > 0) {
            factorial *= temp;
            temp--;
        }
        System.out.println("Factorial of " + number + " = " + factorial);
        
        System.out.println("\n=== Enhanced For Loop (For-Each) ===");
        
        String[] fruits = {"Apple", "Banana", "Orange", "Grape"};
        for (String fruit : fruits) {
            System.out.println("Fruit: " + fruit);
        }
    }
}
