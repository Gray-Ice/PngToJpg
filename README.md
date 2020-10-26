使用本代码需要先安装pillow库:
```shell
pip3 install pillow
```
运行此代码会先获取该py文件同级目录下的文件名，然后创建一个JPGSet文件夹，之后会在JPGSet文件夹下创建所有png文件的jpg格式。
如果你不知道该怎么运行它,这里是命令:
```shell
python3 toJPG.py
```
如果你的系统是windows,那么可能会提示没有pip3和python3这两条命令。确认你安装了python3之后，将pip3和python3替换成pip和python应该就可以了。如:pip install pillow和python toJPG.py

下面是英语版，翻译的不太好。
Before you run this code, you should install pillow for python:
```shell
pip3 install pillow
```
To run this code, use this command:
```shell
python3 toJPG.py
```
It will get the file list at "./", then it will create a directory named "JPGSet".And then, it will create a png file at "JPGSet".
