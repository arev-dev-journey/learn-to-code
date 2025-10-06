/* Section 10
 * Challenge
 * Substitution Cipher
 *
 * A simple and very old method of sending secret messages is the substitution cipher.
 * Basically, each letter of the alphabet gets replaced by another letter of the alphabet.
 * For example, every 'a' get replaced with an 'X', and every 'b' gets replaced with a 'Z', etc.
 *
 * Write a program thats ask a user to enter a secret message
 *
 * Encrypt this message using the substitution cipher and display the encrypted message
 * Then decrypted the the encrypted message back to the original message.
 *
 * You may use the 2 strings below for your substitution
 * For example, to encrypt you can replace the character at position n in alphabet
 * with the character at position n in key
 *
 * To decrypt you can replace the character at position n in key
 * with the character at position n in alphabet
 *
 * Also, currently the cipjer always substitutes a lowercase letter with an uppercase letter and vice-versa.
 *
 */

#include <iostream>
#include <string>

using namespace std;
int main()
{
  string alphabet {"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"};
  string key {"XZNLWEBGJHQDYVTKFUOMPCIASRxznlwebgjhqdyvtkfuompciasr"};

  string secretMessage {};

  cout << "Enter a secret message: " << endl;
  getline(cin, secretMessage);

  string encryptedMessage {};
  for(char c: secretMessage)
  {
    size_t position = alphabet.find(c);
  
  if (position != string::npos)
  {
    char newCharacter {key.at(position)};
    encryptedMessage += newCharacter;
  } else {
    encryptedMessage += c;
  }
  }
  cout << "Secret message is: " << encryptedMessage << endl;
  cout << endl;
  return 0;
}
