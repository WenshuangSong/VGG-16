import os
import random
import shutil
filelist=[]
m_filelist=[]
number=30
inputpath="/home/shijiaying/caffe/data/101_ObjectCategories/"
outputpath="/home/shijiaying/caffe/mjzfile/datatest/"
filelist=os.listdir(inputpath)
for f in filelist:
	FindPath_train=outputpath+"train/"+f+"/" 
	FindPath_val=outputpath+"val/"+f+"/"
	if not os.path.exists(outputpath+"train/"+f+"/"):
		os.makedirs(outputpath+"train/"+f+"/")
	if not os.path.exists(outputpath+"val/"+f+"/"):
		os.makedirs(outputpath+"val/"+f+"/")
	m_filelist=os.listdir(inputpath+f+"/")
	random.shuffle (m_filelist)
	for p in m_filelist[:number]:
		shutil.copyfile(inputpath+f+"/"+p,outputpath+"train/"+f+"/"+p)
	for p in m_filelist[number+1:]:
		shutil.copyfile(inputpath+f+"/"+p,outputpath+"val/"+f+"/"+p)

