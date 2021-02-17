# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:16:39 2021

@author: xwyzworm
"""

import math
messageString = "Halo Coy ini gw nyoba Ciphernya kek mans"
keycode = int(math.floor((math.pow(3,2.5)))) # ini Key daripada Cipher,ini kelemahannya
modeType = "decrypt" # Ubah aja
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
EncryptMessage = "7LWZv2ZjvTYTvRhvYjZMLv2TaSPcYjLvVPVvXLYd"  #ini hasil enkripsi

translatedstr = ""

for message in messageString:
    if message in symbols:
        symindex = symbols.find(message)
        if modeType =='encrypt':
            translatedIndex = symindex + keycode  # ini operasi matematikanya
        elif modeType == "decrypt":
            translatedIndex = symindex - keycode
    
    
        if translatedIndex >= len(symbols):
            translatedIndex = translatedIndex - len(symbols)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(symbols)
            
        
        translatedstr = translatedstr + symbols[translatedIndex]
    else:
        transltedstr = translatedstr + message
        
        
print(translatedstr)
with open("encrypted.txt" ,'w+') as fuf:
    fuf.write(translatedstr)