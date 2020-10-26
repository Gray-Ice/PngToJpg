import os
from PIL import Image

# 获取当前同级目录的文件列表
# get file list in this directory
img_list = os.listdir("./")
# 如果备份文件夹在这个文件夹下就跳过，如果没有备份文件夹就创建
# if the backup directory not in this directory, create it.
if (not (os.path.exists("./JPGSet"))):
	os.mkdir("./JPGSet")

for name in img_list:
    # 如果文件以png结尾
    # if the file is end with png
    if name.endswith(".png"):
        try:
            # 读取文件
            # read the file
            img = Image.open(name)
            # 获取没有后缀名的文件名
            # Get the file name without end name.
            first_name = name[:name.rfind(".")]
            # 将RGBA转换成RGB。A是Alpha，即透明度，JPG不支持透明度，所以如果不转换的话会报错
            # change RGBA to RGB.The meaning of "A" is Alpha, if you don't change it to RGB, PIL will rise an Error.
            img = img.convert('RGB')
            # 保存图片到备份文件夹"JPGSet"下，其后缀名将会变成jpg
            # save the pic to back up directory "JPGSet", it will end with jpg
            img.save("./JPGSet/" + first_name + '.jpg', 'jpeg')
            print(first_name + '.jpg', 'was saved at ./JPGSet.')

        # 捕获无法读取的异常(因为代码我测试过了，可行，所以报IOError应该就是无法读取了)
        # get the IOError.I tested the code, at my computer, it could be run.So if there is some reason to make IOError raise, maybe the file is not a picture or you don't have enough permission.
        except IOError:
            print("This file made IOError:", name)

    else:
        continue
