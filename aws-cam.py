import time
import tinys3 
import picamera
import requests
import json
import ftplib
import os

def aws_upload_image(filename):
    endpoint = "s3-us-west-2.amazonaws.com"
    print("uploading to aws")
    access_key = "AKIAI2QTGXXG6QXJIEJA"
    secret_key = "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"
    file = open(filename,'rb')
    conn = tinys3.Connection(access_key, secret_key, endpoint=endpoint)
    conn.upload(filename,file,'pi-cam-test')
    file.close()
    

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(10) #warmup

    for filename in camera.capture_continuous('images/image{counter:05d}.jpg'):
        print('Captured %s' % filename)
#        upload_image(filename)

        aws_upload_image(filename);
        os.remove(filename)
        time.sleep(10) # wait 5 seconds
        

