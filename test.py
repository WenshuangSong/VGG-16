#coding=utf-8
import sys
sys.path.insert(0,'/home/shijiaying/caffe/python')
import os
import caffe
import numpy as np
GPU_ID = 0
caffe.set_mode_gpu()
caffe.set_device(GPU_ID)
root='/home/shijiaying/caffe/mjzfile/model/'
deploy=root +'VGG_ILSVRC_16_101_deploy_layers.prototxt'
caffe_model=root +'VGG_ILSVRC_16_layers_iter_20255.caffemodel'
import os
import numpy as np
mylist=[]
dir = '/home/shijiaying/caffe/mjzfile/datatest/val/'
filelist=[]
filelist_01=[]
filenames = os.listdir(dir)

for fn in filenames:
    fullfilename = os.path.join(dir,fn)
    filelist.append(fullfilename)
    filenames_01 = os.listdir(fullfilename)
    for f in filenames_01:
	fullfilename_01 = os.path.join(fullfilename,f)
	filelist_01.append(fullfilename_01)

net = caffe.Net(deploy,caffe_model,caffe.TEST)
    # img=root+‘data/DRIVE/test/60337.jpg‘
def Test(img, net):



    # transformer = caffe.io.Transformer({'data':net.blobs['data'].data.shape})
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
    #transformer.set_mean(‘data‘, np.load(mean_file).mean(1).mean(1))
    transformer.set_raw_scale('data', 255)
    transformer.set_channel_swap('data', (2,1,0))
    im=caffe.io.load_image(img)
    net.blobs['data'].data[...] = transformer.preprocess('data',im)


    out = net.forward()
    # labels = np.loadtxt(labels_filename, str, delimiter='\t')
    prob= net.blobs['prob'].data[0].flatten()
    print prob
    order=prob.argsort()[:1]
    #print order
    return prob

    # print 'the class is:',labels[order]
   # f=file("/home/user/swfcode/caffe/label.txt","a+")
    #f.write(labels[order]+'\n')
labels_filename = root +'result.txt'
for i in range(0, len(filelist_01)):
    try:
        img= filelist_01[i]
	print img
	prob=Test(img ,net)
	print np.argmax(prob)
	mylist.append([img,np.argmax(prob)])
    except Exception as e:
	print e 
	continue
file=open('result.txt','w')
for i in mylist:
    file.write(str(i)+'\n')
file.close()


