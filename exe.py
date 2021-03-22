import os
# If you want to run some termainal commands you can use following functions os.chdir and os.system 

path='/home/urname/~~~~~~'   
file_list = os.listdir(path)
print(file_list)
os.chdir('where you have to run a command dir')
for num in range(len(file_list)):
    #print('%s' % file_list[num].split('.')[0])
    os.system('put a command which you want to run')

    
"""    example
path='/home/mooin/yolov5/data/video_0318/side/'
file_list = os.listdir(path)
print(file_list)
os.chdir('/home/mooin/yolov5')
for num in range(len(file_list)):
    #print('%s' % file_list[num].split('.')[0])
    os.system('python3 detect.py --crop --weight best.pt --source data/video_0318/top/%s --name Side_%s' % (file_list[num], file_list[num].split('.')[0]))
"""
