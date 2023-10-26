# Keep-trying
一款基于python的shellcode免杀加载器，Bypass AV

采用网络探测进行简单反沙箱，随机码表base64+随机位移进行加载器和shellcode的加密，并采用分离加载。

## 使用

填写shellcode,运行脚本进行编码

```
python encode.py
```



然后打包load.py
#Pyinstaller
```
pyinstaller -Fw load.py
```
```
#nuitka(需要安装mingw64)
nuitka --mingw64 --standalone --show-progress --follow-imports --onefile --output-dir=out load.py

```
效果
![image-20231026155052662](https://github.com/1fvyuio333/Keep_trying/assets/106239269/85700733-7136-4bf2-a982-4e277d109bb7)
![image-20231026161923197](https://github.com/1fvyuio333/Keep_trying/assets/106239269/792b13c4-f3f7-431e-954a-3dca6088047e)
![image-20231026161809555](https://github.com/1fvyuio333/Keep_trying/assets/106239269/42724e1c-c3d2-4abe-961e-6031b2707976)
