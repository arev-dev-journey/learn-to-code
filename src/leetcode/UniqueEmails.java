/*
 * author: Alex Reveles
 * date: 2024-10-20
 * description: Given an array  of strings, emails, write a function
 * that returns the number of unique emails that will actually receive mail
 */
import java.util.Set;
import java.util.HashSet;

public class UniqueEmails {
  public int numUniqueEmails(String[] emails) {
    // Initialize an empty set of unique emails
    Set<String> uniqueEmails = new HashSet<>();

    // Loop through the emails input array
    for (String email : emails) {

      // Split the email at the '@' to separate the local name from the domain name
      String[] parts = email.split("@");
      String local = parts[0];
      String domain = parts[1];

      // For the local name: a. remove everything after the first '+' (if present)
      if (local.contains("+")) {
        local = local.substring(0, local.indexOf('+'));
      }
      // b. remove all '.' in the remaining parts
      local = local.replace(".", "");

      // Recombine the processed local name and domain name
      String processedEmail = local + "@" + domain;
      // Add the processed email to the set
      uniqueEmails.add(processedEmail);
    }
    // After processing, return the size of the set
    return uniqueEmails.size();
  }

  public static void main(String[] args) {
    UniqueEmails solution = new UniqueEmails();

    String[] emails = {
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    };

    System.out.println(solution.numUniqueEmails(emails)); // Output: 2
  }
}
