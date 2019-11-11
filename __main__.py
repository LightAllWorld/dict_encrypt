from encrypt_and_decrypt import *


if __name__ == '__main__':
    while True:
        command = input("Enter the command. \
                        (1) Encryption \
                        (2) Decryption \
                        (3) Exit")
                        
        if command == "3" or command == "Exit":
            break
        
        # if you want another key, have to enter the key.
        # The key must be one of length 128, 192, or 256 bits.
        
        key = input("Enter the key.")

        if key:
            if len(key) == 128 or len(key) == 192 or len(key) == 256:
                pass
            else:
                print("Key length error. Please check your key length.\
                      key must be one of length 128, 192 or 256 bits.")
                continue
                
        if command == "1" or command == "Encryption":
            plain_text = input("Enter the text you want to encrypt.")
            if key:
                encryted_text = encryption(plain_text, key)
            else:
                encryted_text = encryption(plain_text)
            print(encryted_text)
            
        elif command == "2" or command == "Decryption":
            encrypted_text = input("Enter the text you want to decrypt")
            if key:
                decrypted_text = decrytion(encrypted_text, key)
            else:
                decrypted_text = decrytion(encryption_text)
            print(decrypted_text)
        else:
            print("Bad Command.")
            
