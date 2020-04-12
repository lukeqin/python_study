#-*- coding: UTF-8 -*-
'''
Created on 2017年3月13日
@author: luke
'''

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class endecrypt():
    def __init__(self, key):
        self.key = self.key_text_length(key)
        self.mode = AES.MODE_CBC

    def key_text_length(self, data):
        length = 16
        count = len(data)
        add = length - (count % length)
        data = data + ('\0' * add)
        return data

    def myencrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        textadd = self.key_text_length(text)
        return b2a_hex(cryptor.encrypt(textadd))
        
    def mydecrypt(self, encrypt_text):
        cryptor = AES.new(self.key, self.mode, self.key)
        return cryptor.decrypt(a2b_hex(encrypt_text))


if __name__ == '__main__':
    while True:
        key = raw_input("Please input your key [q:quit] : ")
        if key == "":
            print "Key can not be empty. "
        elif key == "q":
            exit(0)
        else:
            ende = endecrypt(key)
            endetype = raw_input("Please input 'en' to encrypt passwd or 'de' to decrypt passwd : ")
            if endetype == "en":
                passwd = raw_input("Please input your passwd : ")
                print ende.myencrypt(passwd)
            elif endetype == "de":
                depasswd = raw_input("please input your encrypted passwd: ")
                print ende.mydecrypt(depasswd)
    
    '''
               程序是在centos写的，windows安装的Crypto不能导入AES。
    [root@zc opt]# python2.6 endecrypto.py 
    Please input your key [q:quit] : 123456
    Please input 'en' to encrypt passwd or 'de' to decrypt passwd : en
    Please input your passwd : 808080
    b2b4380b7c8155a6baf99e72584c25a5
    Please input your key [q:quit] : 123456
    Please input 'en' to encrypt passwd or 'de' to decrypt passwd : de
    please input your encrypted passwd: b2b4380b7c8155a6baf99e72584c25a5
    808080
    Please input your key [q:quit] : q
    [root@zc opt]# 
    '''


    '''
    p = endecrypt("123456")
    en = p.myencrypt("123456")
    print en

    de = p.mydecrypt(en)
    print de
    '''


