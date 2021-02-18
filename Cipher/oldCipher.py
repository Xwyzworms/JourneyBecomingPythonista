def encryptext(text,shift = 13):
    
    lowerAlpha = "abcdefghijklmnopqrstuvwxyz"
    upperAlpha = lowerAlpha.upper()
    numbers = "0123456789"

    realTable = lowerAlpha  + upperAlpha + numbers
    modifiedTable = lowerAlpha[shift:] + lowerAlpha [:shift]+\
            upperAlpha[shift:] + upperAlpha[:shift] +\
            numbers[shift:] + numbers[:shift]

    getModifiedTable = str.maketrans(realTable,modifiedTable)
    oldCipher=text.translate(getModifiedTable)

    print("Coded \n")
    print("Actual : {}".format(text))
    print("Cipher :  {}".format(oldCipher))

    getModifiedTable = str.maketrans(modifiedTable,realTable)
    ActualMessage = oldCipher.translate(getModifiedTable)
    print(" Decrypted cipher :  {}".format(ActualMessage))


if __name__ == "__main__":
    encryptext("Pram Tolol")   