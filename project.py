import os,sys
import time
#sys.path.append('/home/Social_Distance/darknet/')
sys.path.append('/home/Social_Distance/darknet')

#import darknet as dn
import pdb
import shutil
import numpy as np
import cv2
from darknet import performDetect #use darknet not darknetAB as I renamed it to avoid confusion with PJs

#net = dn.load_net(b'/home/peter/darknet/cfg/yolov3-tiny_pdq.cfg',b'/home/peter/darknet/backup/yolov3-tiny_pdq_25700.weights',0)
#meta = dn.load_meta(b'/home/peter/darknet/data/pdq_obj.data')
cfg_file = "/home/Social_Distance/darknet/cfg/yolo-obj.cfg"
obj_file = "/home/Social_Distance/darknet/data/obj.data"
weights = "/home/Social_Distance/darknet/backup/yolov3_900.weights"
folder = "/home/Social_Distance/darknet/output"
thresh  = 0.25

while True:
   files = os.listdir(folder)
   #dn.detect fails occasionally. I suspect a race condition.
   time.sleep(5)
   for f in files:
       if f.endswith(".png"):
           print (f)
           path = os.path.join(folder, f)
           pathb = path.encode('utf-8')
           #res = dn.detect(net, meta, pathb)
           try:
              res=performDetect(folder+"/"+f,thresh,cfg_file,weights,obj_file,False,True,False)
              print (res) #list of name, probability, bounding box center x, center y, width, height
              i=0
              new_path = '/home/Social_Distance/darknet/output/none/'+f #initialized to none
              img = cv2.imread(path,cv2.IMREAD_COLOR) #load image in cv2
              while i<len(res):
                  res_type = res[i][0]      
                  if "person moving" in res_type:
                      #copy file to person directory
                      new_path = '/home/Social_Distance/darknet/output/person_moving/'+f
                      #set the color for the person bounding box
                      box_color = (0,255,0)
                  elif "person walking" in res_type:
                      new_path = '/home/Social_Distance/darknet/output/person_walking'+f
                      box_color = (0,255,255)
                  elif "person setting" in res_type:
                      new_path = '/home/Social_Distance/darknet/output/person_setting'+f
                      box_color = (255,0,0)
                  elif "bag" in res_type:
                      new_path = '/home/Social_Distance/darknet/output/bage'+f
                      box_color = (0,0,255)
                  #get bounding box
                  center_x=int(res[i][2][0])
                  center_y=int(res[i][2][1])
                  width = int(res[i][2][2])
                  height = int(res[i][2][3])
               
                  UL_x = int(center_x - width/2) #Upper Left corner X coord
                  UL_y = int(center_y + height/2) #Upper left Y
                  LR_x = int(center_x + width/2)
                  LR_y = int(center_y - height/2)
               
                  #write bounding box to image
                  cv2.rectangle(img,(UL_x,UL_y),(LR_x,LR_y),box_color,1)
                  #put label on bounding box
                  font = cv2.FONT_HERSHEY_SIMPLEX
                  cv2.putText(img,res_type,(center_x,center_y),font,2,box_color,2,cv2.LINE_AA)
                  i=i+1
              cv2.imwrite(new_path,img) #wait until all the objects are marked and then write out.
              #todo. This will end up being put in the last path that was found if there were multiple
              #it would be good to put it all the paths.
              try:
                 os.remove(path) #remove the original
              except FileNotFoundError as err:
                 print (err) #file may have been removed by another process
           except ValueError as err:
              print (err)
           
