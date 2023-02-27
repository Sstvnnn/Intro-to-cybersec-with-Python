def encrypt(plaintext, key):
  ciphertext = ""
  # Loop through each character in the plaintext
  for char in plaintext:
      # Check if the character is an alphabetic character
      if char.isalpha():
          # Calculate the shift value by adding the key to the character's ASCII code
          shift = ord(char) + key
          # Check if the character is uppercase
          if char.isupper():
              # If the shift value is greater than the ASCII code for 'Z', wrap around to the beginning of the alphabet
              if shift > ord("Z"):
                  shift -= 26
                  #shift = shift % 90 + 65
              # If the shift value is less than the ASCII code for 'A', wrap around to the end of the alphabet
              elif shift < ord("A"):
                  shift += 26
                  #shift = shift % 90 + 65
              # Add the shifted character to the ciphertext string
              ciphertext += chr(shift)
          # If the character is lowercase
          else:
              # If the shift value is greater than the ASCII code for 'z', wrap around to the beginning of the alphabet
              if shift > ord("z"):
                  shift -= 26
              # If the shift value is less than the ASCII code for 'a', wrap around to the end of the alphabet
              elif shift < ord("a"):
                  shift += 26
              # Add the shifted character to the ciphertext string
              ciphertext += chr(shift)
      # If the character is not alphabetic
      else:
          # Add the character to the ciphertext string as is
          ciphertext += char
  
  # Return the ciphertext string
  return ciphertext


def decrypt(ciphertext, key):
  plaintext = ""
  # Loop through each character in the ciphertext
  for char in ciphertext:
      # Check if the character is an alphabetic character
      if char.isalpha():
          # Calculate the shift value by subtracting the key from the character's ASCII code
          shift = ord(char) - key #Kesebelah Kiri
          # Check if the character is uppercase
          if char.isupper():
              # If the shift value is greater than the ASCII code for 'Z', wrap around to the beginning of the alphabet
              if shift > ord("Z"):
                  shift -= 26
              # If the shift value is less than the ASCII code for 'A', wrap around to the end of the alphabet
              elif shift < ord("A"):
                  shift += 26
              # Add the shifted character to the plaintext string
              plaintext += chr(shift)
          # If the character is lowercase
          else:
              # If the shift value is greater than the ASCII code for 'z', wrap around to the beginning of the alphabet
              if shift > ord("z"):
                  shift -= 26
              # If the shift value is less than the ASCII code for 'a', wrap around to the end of the alphabet
              if shift < ord("a"):
                  shift += 26
              # Add the shifted character to the plaintext string
              plaintext += chr(shift)
      # If the character is not alphabetic
      else:
          # Add the character to the plaintext string as is
          plaintext += char
  
  # Return the plaintext string
  return plaintext

# Example usage of our encryption and decryption functions
key = 32
plaintext = "This is a secret mEsSaGe!"
# plain = decrypted
# cipher = encrypted

def  main():
    while True:
        choice = input("Enter your choice : ")
        if choice == '1':
            ciphertext = encrypt(plaintext, key)
            print("Encrypted message:", ciphertext)
        elif choice == '2':
            decrypted_text = decrypt(ciphertext, key)
            print("Decrypted message:", decrypted_text)
        elif choice == '3':
            file_name = input("Enter File Name : ")
            try :
                with open(f"{file_name}.txt", 'r') as f :
                    cipher__text = f.read()
                decrypted__text = decrypt(cipher__text,key)
                print("Decryted message from this file :", decrypted__text)
            except FileNotFoundError :
                print("There's no file")
                with open(f"{file_name}.txt", 'w') as f:
                   plain_text = input("Enter Plain text to encrypt : ")
                   cipher_text = encrypt(plain_text,key)
                   f.write(cipher_text)
                
if __name__ == '__main__' :
    main()

  