# port data from csv camers
# test
# develop by F.A.T 
###################################################################
import cv2
import time
import darknet_images
import os
import time
from camCal import *
##################################################################3



def cctvDetect(counter):
    open_space = 'rtsp://cctv:cctv@172.18.20.204:554/cam1/h264-1'
    Dyson1 = 'rtsp://cctv:cctv@172.18.20.209:554/cam1/h264-1'
    dyson2 = 'rtsp://cctv:cctv@172.18.20.210:554/cam1/h264-1'
    Admin = 'rtsp://cctv:cctv@172.18.20.215:554/cam1/h264-1'
    capture = cv2.VideoCapture(Admin)
    ID = 204 # open_space id
    print('Warring!! online CCTV monitoring don\'t press any key . . . . . .   ')
    print('Used CCTV id: ', ID)
    ret, frame = capture.read()
    print('frame captured successfully')
    #cv2.imwrite('/mnt/k/camCal/{}4online_{}.png'.format(ID,counter),frame)# store the image
    insertImage(frame,counter,ID)
    #cv2.imshow('frame',frame)
    capture.release()
    cv2.destroyAllWindows()

#################################################################
### testing area
#j = 0 ;
#while(True):
    #j+=1
    #cctvDetect(j)
    #time.sleep(2)
    
