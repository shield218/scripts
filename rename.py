import os
from shutil import copyfile
path="C:/Users/shield616/Desktop/youku_data/"
#dir=os.getcwd()     #文件路径
def renamefiles():
    
    ldst=path+'l/'
    rdst=path+'r/'
    src=path+'image/'
    if not(os.path.isdir(rdst)):
        os.mkdir(rdst)
    if not(os.path.isdir(ldst)):
        os.mkdir(ldst)

    wildcard = ".jpg"
    start=1
    end=38

    for i in range(start,end+1):
        o_name = str(i) + wildcard
        l_name0 = str(format(i,'0>6d')) + '_10' + wildcard
        l_name1 = str(format(i,'0>6d')) + '_11' + wildcard
        r_name0 = str(format(i-1,'0>6d')) + '_10' + wildcard
        r_name1 = str(format(i-1,'0>6d')) + '_11' + wildcard

        l_name0 = os.path.join(ldst,l_name0)
        r_name0 = os.path.join(rdst,r_name0)
        l_name1 = os.path.join(ldst,l_name1)
        r_name1 = os.path.join(rdst,r_name1)
        o_name = os.path.join(src,o_name)

        if(os.path.isfile(o_name)):
            if i<end:
                copyfile(o_name,l_name0)
                copyfile(o_name,l_name1)
            if i>start:
                copyfile(o_name,r_name0)
                copyfile(o_name,r_name1)

renamefiles()