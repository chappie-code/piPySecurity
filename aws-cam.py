#!/usr/bin/env python

import time
import tinys3 
import picamera
import requests
import json
import ftplib
import os
import config



def aws_upload_image(filename):
    endpoint = "s3-us-west-2.amazonaws.com"
    print("uploading to aws")
    access_key = config.access_key
    secret_key = config.secret_key
    file = open(filename,'rb')
    conn = tinys3.Connection(access_key, secret_key, endpoint=endpoint)
    conn.upload(filename,file,'pi-cam-test')
    file.close()
    

with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.rotation = 180
    time.sleep(10) #warmup
    count_list = list(range(0,48))
    for val in count_list:
       filename = 'images/image_'+str(val)+'.jpg'
       camera.capture(filename)
       aws_upload_image(filename)
       os.remove(filename)
       time.sleep(30)

    camera.stop_preview()

    
        

