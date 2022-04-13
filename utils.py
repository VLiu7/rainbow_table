import hashlib
import random
import string
from config import get_config
from argon2 import PasswordHasher


Config=get_config()
def H(plaintext):
    return hashlib.sha256(bytes(plaintext,'utf-8')).hexdigest()
def R(hash,col):
    tmp=int(hash,16)^col
    x=random.randint(0,len(Config.LETTER_SET)-1)
    length=0
    text=""
    if x==0:
        length=Config.MIN_PW_LENGTH
    else:
        length=Config.MAX_PW_LENGTH
    for i in range(length):
        text += Config.LETTER_SET[tmp%len(Config.LETTER_SET)]
        tmp //=len(Config.LETTER_SET)
    return text

def generate_password():
    x=random.randint(0,len(Config.LETTER_SET)-1)
    length=0
    password=""
    if x==0:
        length=Config.MIN_PW_LENGTH
    else:
        length=Config.MAX_PW_LENGTH
    for _ in range(length):
        password += random.choice(Config.LETTER_SET)
    return password
    
if __name__ == '__main__':
    password=generate_password()
    # print(password)
    hash=H(password)
    print(hash)
    text=R(hash,0)
    print(text)