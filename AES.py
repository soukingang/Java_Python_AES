from Crypto.Cipher import AES
import os
import base64
from itsdangerous import base64_encode, base64_decode

BS = AES.block_size
print(BS)
pad = lambda s: s + bytes([BS - len(s) % BS]) * (BS - len(s) % BS)
unpad = lambda s: s[0:-ord("%c" % s[-1])]

key = b'1234567890123456'
iv = b'1234567890123456'

text_lt = b'1234567890'
text_eq = b'1234567890abcdef'
text_gt = b'1234567890abcdef123456'

cipher = AES.new(key, AES.MODE_CBC, IV=iv)
data_lt = base64.b64encode(cipher.encrypt(pad(text_lt)))
print("原字符串是: %s" % str(text_lt, encoding = "utf-8"))
print("加密后的字串是: %s" % str(data_lt, encoding = "utf-8"))
cipher = AES.new(key, AES.MODE_CBC, IV=iv)
print("解密后的字串是: %s" % str(unpad(cipher.decrypt(base64_decode(data_lt))), encoding='utf-8'))

cipher = AES.new(key, AES.MODE_CBC, IV=iv)
data_eq = base64.b64encode(cipher.encrypt(pad(text_eq)))
print("原字符串是: %s" % str(text_eq, encoding = "utf-8"))
print("加密后的字串是: %s" % str(data_eq, encoding = "utf-8"))
cipher = AES.new(key, AES.MODE_CBC, IV=iv)
print("解密后的字串是: %s" % str(unpad(cipher.decrypt(base64_decode(data_eq))), encoding='utf-8'))


cipher = AES.new(key, AES.MODE_CBC, IV=iv)
data_gt = base64.b64encode(cipher.encrypt(pad(text_gt)))
print("原字符串是: %s" % str(text_gt, encoding = "utf-8"))
print("加密后的字串是: %s" % str(data_gt, encoding = "utf-8"))
cipher = AES.new(key, AES.MODE_CBC, IV=iv)
print("解密后的字串是: %s" % str(unpad(cipher.decrypt(base64_decode(data_gt))), encoding='utf-8'))
