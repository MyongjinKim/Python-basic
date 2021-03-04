import os
file_path = ~/blablabla  ##put your file path which includes all what you wanna change name at the same time
file_names =os.listdir(file_path)  ## you can take all file list included your file_path

i=1

for name in file_names:        ##you can put the number in order in your class
    src = os.path,join(file_path, name)
    dst = 'abcd' + '.aaa' #you can add or change its name or format
    dst = os.path.join(file_path, dst)
    os.rename(src,dst)
    i+=1

##example

#import os
#file_path = ~/Downloads/train_images
#file_names =os.listdir(file_path)  
#
#i=1
#
#for name in file_names:       
#    src = os.path,join(file_path, name)
#    dst = 'cup' + '.jpg' 
#    dst = os.path.join(file_path, dst)
#    os.rename(src,dst)
#    i+=1

