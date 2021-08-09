#!/bin/sh


for i in
udo python3 darknet_images.py --input /mnt/k/Social_Distance/dataSet/TES_DATA_00028.png --batch_size 1 --weights /home/Social_Distance/darknet/backup/yolo-obj_last_800.weights  --config_file /home/Social_Distance/darknet/cfg/yolo-obj.cfg --data_file /home/Social_Distance/darknet/data/obj.data
