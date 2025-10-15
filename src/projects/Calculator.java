/**
 * Simple Calculator Project
 * A basic calculator implementation to demonstrate Java OOP concepts
 */
public class Calculator {
    private double result;
    
    public Calculator() {
        this.result = 0.0;
    }
    
    public double add(double num1, double num2) {
        result = num1 + num2;
        return result;
    }
    
    public double subtract(double num1, double num2) {
        result = num1 - num2;
        return result;
    }
    
    public double multiply(double num1, double num2) {
        result = num1 * num2;
        return result;
    }
    
    public double divide(double num1, double num2) {
        if (num2 == 0) {
            throw new IllegalArgumentException("Cannot divide by zero");
        }
        result = num1 / num2;
        return result;
    }
    
    public double getResult() {
        return result;
    }
    
    public void clear() {
        result = 0.0;
    }
    
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        System.out.println("Calculator Demo:");
        System.out.println("10 + 5 = " + calc.add(10, 5));
        System.out.println("10 - 5 = " + calc.subtract(10, 5));
        System.out.println("10 * 5 = " + calc.multiply(10, 5));
        System.out.println("10 / 5 = " + calc.divide(10, 5));
    }
}
