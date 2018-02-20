import os
import csv
namelist=[]
labellist=[]
number=30
count=-1
inputpath="/home/shijiaying/caffe/mjzfile/datatest/train/"
outputpath="/home/shijiaying/caffe/mjzfile/datatest/"
dir_list=os.listdir(inputpath)
for d  in dir_list:
	count = count+1
	FindPath=inputpath+d+"/"
	filelist=os.listdir(FindPath) 
	for name in filelist:  
		labellist.append(count)
		namelist.append(os.path.join(FindPath,name))     
print len(namelist), len(labellist)
with open(outputpath+'train.txt', 'w') as h:
    for f1, f2 in zip(namelist, labellist):
        print  >> h, f1, f2

