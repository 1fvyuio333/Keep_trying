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
