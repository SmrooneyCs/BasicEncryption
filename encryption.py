#Sean Rooney
#7/7/2022
#This program encrypts and decrypts bsaed on a library


def encrypt_file(file_choice):
    encryption_key =  { "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7",
                        "h": "8", "i": "9", "j": ">","k": "<", "l": ".", "m": "!", "n": "#",
                        "o": "%", "p": "?", "q": "+", "r": "*", "s": "&", "t": "`",
                        "u": "@", "v": "_", "w": "-", "x": "$", "y": "/", "z": ";" , " ": "~"}      # The dictionary with the keys and values to encrypt with.

    encrypted_txt = ''                                                                              # An empty string to append the altered character onto.

    try:
        with open(file_choice) as f:                                                                    # opening a file
            for line in f:                                                                              # getting each line from the file.
                for ch in line.lower():                                                                 # getting each character from the file and making sure its lower case.
                    if ch in encryption_key:                                                            # condition to check what character matches what key and then appends the associated value of that key to the empy string.
                        encrypted_txt += str(encryption_key[ch])
                    else:                                                                               # if the condition is not met we append that character anyway.
                        encrypted_txt += ch
    except FileNotFoundError:
        print("File does not exist")
        exit()

    with open('Encryptedfile.txt','w')as en:                                                        # writing the contents of the string "encrypted_txt" to a new file.
        en.write(encrypted_txt)

    print("done\n")                                                                                 # printing to know when this function completes.



def decrypt_file(file_choice):
    encryption_key =  { "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7",
                        "h": "8", "i": "9", "j": ">","k": "<", "l": ".", "m": "!", "n": "#",
                        "o": "%", "p": "?", "q": "+", "r": "*", "s": "&", "t": "`",
                        "u": "@", "v": "_", "w": "-", "x": "$", "y": "/", "z": ";" , " ": "~"}
    
    decrypted_text = ''
    
    try:
        with open(file_choice) as f:                                                                    # Opening the file passed.
            ch_list = []                                                                                # creating a new list to store each character in from the file.
            for line in f:
                for ch in line:
                    ch_list.append(ch)
    except FileNotFoundError:
        print("File not found")
    
    
    
    for ch in ch_list:                                                                              # Looping through the character list.
        for key, value in encryption_key.items():                                                   # Assigning each Key and value to variables for iteration.
            if value == ch:                                                                         # checking if the condition is true, if it is append the key to the blank string.
                decrypted_text += key
            
                
    
    print(decrypted_text)                                                                           # Printing the decrypted string.
    
def main():                                                                                         #defining a main function to call all of my functions.
    print("Encrypting file:")
    encrypt_file("Test.txt")
    
    print("Decrypting the same file:")
    decrypt_file('Encryptedfile.txt')
    
main()                                                                                      
    
                    