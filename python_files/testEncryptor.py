from random import *

def encryptor():
    string = input("""Please enter a string for encryption:
""")
    print(string)
    stringLength = len(string)
    shiftKey = []
    for a in range(stringLength):
        shiftKey.append(randint(1, 9))
    encryptedString = ""
    for b in range(stringLength):
        value = ord(string[b])
        encryptedString += chr(value + shiftKey[b])
    key = ""
    for c in range(stringLength-1, -1, -1):
        key += str(shiftKey[c])
    print("")
    print(encryptedString)
    print("")
    print(key)
    pause = input()

def decryptor():
    encryptedString = input("""Please enter the encrypted string exactly as given:
""")
    encryptedStringLength = len(encryptedString)
    key = input("""Please enter the key exactly as given:
""")
    shiftKey = []
    for a in range(encryptedStringLength-1, -1, -1):
        shiftKey.append(int(key[a]))
    oldString = ""
    for b in range(encryptedStringLength):
        value = ord(encryptedString[b])
        oldString += chr(value - shiftKey[b])
    print("")
    print( oldString )
    pause = input()

encryptor()

decryptor()
