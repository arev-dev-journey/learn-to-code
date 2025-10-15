/**
 * Basic Java Variables and Data Types Practice
 */
public class VariablesAndTypes {
    public static void main(String[] args) {
        // Primitive data types
        byte byteValue = 127;
        short shortValue = 32000;
        int intValue = 2147483647;
        long longValue = 9223372036854775807L;
        
        float floatValue = 3.14f;
        double doubleValue = 3.14159265359;
        
        boolean booleanValue = true;
        char charValue = 'A';
        
        // String (reference type)
        String stringValue = "Hello, Java!";
        
        // Display all values
        System.out.println("Byte: " + byteValue);
        System.out.println("Short: " + shortValue);
        System.out.println("Int: " + intValue);
        System.out.println("Long: " + longValue);
        System.out.println("Float: " + floatValue);
        System.out.println("Double: " + doubleValue);
        System.out.println("Boolean: " + booleanValue);
        System.out.println("Char: " + charValue);
        System.out.println("String: " + stringValue);
        
        // Type conversion examples
        int convertedInt = (int) doubleValue;
        System.out.println("Double to Int: " + convertedInt);
    }
}
