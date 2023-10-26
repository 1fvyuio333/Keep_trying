# Keep-trying
一款基于python的shellcode免杀加载器，Bypass AV



## 使用

填写shellcode,运行脚本进行编码

```
python encode.py
```



然后打包load.py
#Pyinstaller
```
nuitka --mingw64 --standalone --show-progress --follow-imports --onefile --output-dir=out moon_kill.py

```
