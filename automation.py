import os
import time
from cctv import *

for i in range(0,10000000000):
    cctvDetect(i)# run cctv
    time.sleep(2)
    os.system('sudo python3 darknet_images.py --input /mnt/k/monitoring/204online_{}.png --batch_size 1 --weights /home/Social_Distance/darknet/backup/yolo-obj_last.weights  --config_file /home/Social_Distance/darknet/cfg/yolo-obj.cfg --data_file /home/Social_Distance/darknet/data/obj.data --dont_show'.format(i))

    if(i>0):
        os.system('sudo rm /mnt/k/monitoring/204online_{}.png'.format(i-1))

