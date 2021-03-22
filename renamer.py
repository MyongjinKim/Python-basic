import os
file_path = ~/blablabla  ##put your file path which includes all what you wanna change name at the same time in sequence
file_names =os.listdir(file_path)  ## you can take all file list included your file_path

i=1

for name in file_names:        ##you can put the number in order in your class
    src = os.path,join(file_path, name)
    dst = 'abcd' + '.aaa' #you can add or change its name or format
    dst = os.path.join(file_path, dst)
    os.rename(src,dst)
    i+=1

"""example

import os

path='/home/mooin/yolov5/runs/detect/Side/'

file_list = os.listdir(path)

for num in range(len(file_list)):
    file_path = os.path.join(path,file_list[num])
    file_path = file_path + '/crop'
    file_names =os.listdir(file_path)
    folder_name = file_list[num]
    i=1
    for name in file_names:   
        src = os.path.join(file_path,name)
        dst = folder_name + '_' + name.split('-')[0] + str(i) + '.jpg'
        dst = os.path.join(file_path,dst)
        os.rename(src,dst)
        i+=1

"""
