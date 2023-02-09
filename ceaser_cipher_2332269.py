def welcome():
  '''This function simply
print an introduction
to the user about program
'''
  print('Welcome to the Caesar Cipher')
  print('This program encrypts and decrypts text with the Caesar Cipher')

def enter_message():
  '''This function request user to determine mode of
conversion and the message that they would like to encrypt or decrypt.
This function check if the mode the user entered is valid .
This function return mode and message. The message is converted to upper case to avoid potential
encrypting/decrypting issues
'''
  while True:
    # Prompt user to select a mode
    mode = input("Would you like to encrypt (e) or decrypt (d): ")
    if mode !='e' and mode!='d':
      print('Invalid mode')
      continue

    if mode.lower() =='e':
      message=input("What message would you like to encrypt:")
      #To convert the entered message into uppercase
      message=message.upper()
      
    elif mode.lower() =='d':
      message=input("What message would you like to decrypt:")
      #To convert the entered message into uppercase
      message=message.upper()

    return mode, message

def encrypt(message, shift):
  '''This function encrypt a plain text message as encrypted
text. It takes 2 parameters, the message to be encrypted, and the shift number
'''
 
  # Encrypt the message 
  output = ""
  for letter in message:
    if letter.isalpha():
      # Get the ASCII code of the letter
      ascii_code = ord(letter)

      # Shift the ASCII code
      ascii_code += shift

      # Handle the encryption if letter becomes greater tha Z
      if ascii_code > ord('Z'):
        ascii_code -= 26

      # Add the encrypted letter to the output
      output += chr(ascii_code)
    else:
      # Add non-letter characters to the output unchanged
      output += letter

  return output

def decrypt(message, shift):
  '''This function decrypt a message.
It takes 2 parameters, the message to be decrypted, and the shift
number
'''
  # Decrypt the message using Caesar cipher
  output = ""
  for letter in message:
    if letter.isalpha():
      # Get the ASCII code of the letter
      ascii_code = ord(letter)

      # Shift the ASCII code
      ascii_code -= shift

      # Handle the if letter becomes lesser than A after decryption 
      if ascii_code < ord('A'):
        ascii_code += 26

      # Add the decrypted letter to the output
      output += chr(ascii_code)
    else:
      # Add non-letter characters to the output unchanged
      output += letter

  return output

def main():
  '''This function prompt users to select a mode, check if mode is valid
or not, prompt user the message to be encrypted or decrypted,
encrypt and decrypt the message and display output.
Ask user if they want to continue whether they want to continue further
'''
  while True:
    # Get the mode and message from the user
    mode, message = enter_message()

    # Prompt user for shift number
    shift = int(input("Enter the shift number: "))

    # Encrypt or decrypt the message
    if mode == 'e':
      output = encrypt(message, shift)
    else:
      output = decrypt(message, shift)

    # Print the output
    print('Output:',output)

    # Prompt user to go again
    again = input("Encrypt or decrypt another message? (y/n) ")

    # Check if the user wants to go again
    if again!= 'y':
      break
  print('Thanks for using the program, goodbye!')
         
welcome()
main()
