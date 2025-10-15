import java.util.HashSet;
import java.util.Set;

public class UniqueEmail {
  public int numUniqueEmails(String[] emails) {
    Set<String> uniqueEmails = new HashSet<>();

    for (String email : emails) {
      String[] parts = email.split("@");
      String local = parts[0];
      String domain = parts[1];

      // Process local parts and ignore everything after '+' and remove '.'
      if (local.contains("+")) {
        local = local.substring(0, local.indexOf("+"));
      }
      local = local.replace(".", "");

      // Reconstruct the email and to set
      String processesEmail = local + "@" + domain;
      uniqueEmails.add(processesEmail);
    }
    return uniqueEmails.size();
  }

  public static void main(String[] args) {
    UniqueEmail solution = new UniqueEmail();

    String[] emails = {
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
        "ajreveles0@gmail.com",
        "a.j.reveles1+35@gmail.com"
    };
    System.out.println(solution.numUniqueEmails(emails));
  }
}
