#####################################################################################################################################
# CCTV cam calibration 
# 21/March/2021
# Developd by: FATHI MAHDI ELSIDDIG HAROUN
# Private Software
####################################################################################################################################
import cv2
import os
import numpy as np
import glob
#####################################################################################################################################

#image_path = '/mnt/k/camCal/215online_24.png'
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
#objp = np.zeros((9*6,3), np.float32)
objp = np.zeros((7*4,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:4].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


def findCornersPath(image_path):
    image = cv2.imread(image_path)
    new_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('2153.png',new_image)
    #etval, corners = cv2.findChessboardCorners(new_image,(9,6),flags=cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
    etval, corners = cv2.findChessboardCorners(new_image,(7,4),flags=cv2.CALIB_CB_ADAPTIVE_THRESH)
    #print(corners)
    cv2.waitKey(20)
    cv2.destroyAllWindows()
    return new_image,etval,corners

def findCornersImg(image):
    new_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('2153.png',new_image)
    etval, corners = cv2.findChessboardCorners(new_image,(7,4),flags=cv2.CALIB_CB_ADAPTIVE_THRESH)
    #print(corners)
    cv2.waitKey(20)
    cv2.destroyAllWindows()
    return new_image,etval,corners

def calPath(image_path,gray,objpoints, imgpoints,counter,ID):
    img = cv2.imread(image_path)
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
    h,  w = img.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
    mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
    dst_new = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
    # crop the image
    x,y,w,h = roi
    crop_dst = dst[y:y+h, x:x+w]
    #cv2.imwrite('/mnt/k/camCal/calibresult{}_{}.png'.format(counter,ID),dst)
    cv2.imwrite('/mnt/k/monitoring/{}online_{}.png'.format(ID,counter),crop_dst)
    print('frame calabrated and stored!!')

def calImg(img,gray,objpoints, imgpoints,counter,ID):
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
    h,  w = img.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
    mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
    dst_new = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
    # crop the image
    x,y,w,h = roi
    crop_dst = dst[y:y+h, x:x+w]
    #cv2.imwrite('/mnt/k/camCal/calibresult{}_{}.png'.format(counter,ID),dst)
    cv2.imwrite('/mnt/k/monitoring/{}online_{}.png'.format(ID,counter),crop_dst)
    print('frame calabrated and stored!!')

def insertImage(img,counter,ID):
    image_path = '/mnt/k/camCal/2044online_98.png' # standard image for online clalibration
    gray,etval,corners = findCornersPath(image_path)
    objpoints.append(objp)
    corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
    imgpoints.append(corners2)
    calImg(img,gray,objpoints,imgpoints,counter,ID)

def undist(image):
    f = open('CamCalData.dat','r')
    f.close()


def testAll():
    for i in range(1,145):
            image_path = '/mnt/k/camCal/2044online_{}.png'.format(i)
            img = cv2.imread(image_path)
            gray,etval,corners = findCornersPath(image_path)
            if (etval == True):
                print('found it at: ',i)
                objpoints.append(objp)
                corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
                imgpoints.append(corners2)
                img = cv2.drawChessboardCorners(img, (9,6), corners2,etval)
                cv2.imshow('img{}'.format(i),img)
                cv2.imwrite('/mnt/k/camCal/openspace_2044{}.png'.format(i),img)
                cv2.waitKey(500)


def testImage(image_path):
        ori_img = cv2.imread(image_path)
        gray,etval,corners = findCornersPath(image_path)
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        img = cv2.drawChessboardCorners(ori_img, (7,6), corners2,etval)
        calPath(image_path,gray,objpoints,imgpoints,0)



##########################################################################
# testing area
#image_path = '/mnt/k/camCal/2158online_54.png'
#img = cv2.imread(image_path)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#insertImage(img,54,2158)
##############################################################################
