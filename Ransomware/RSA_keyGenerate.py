# pip install pycryptodome
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
from Crypto.PublicKey import RSA


key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.export_key()

with open("private.pem",'wb') as fuf:
    fuf.write(private_key)

with open("public.pem",'wb') as fuf:
    fuf.write(public_key)

