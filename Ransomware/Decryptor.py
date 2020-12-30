from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

enc_
private_key = RSA.import_key(open('private.pem').read())
#decyprtor

private_decryptor = PKCS1_OAEP.new(private_key)

#Decrypted Session key

dec_fernet_key = private_decryptor.decrypt(Decrypt_fernet_key)


print(f"Private key : {private_key}")
print(f"Private Decryptor : {private_decryptor}")
print(f"Decrypted fernet key :  {dec_fernet_key}")
print(f"ITULAH MEMANG")