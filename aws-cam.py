import time
import tinys3 
import picamera
import requests
import json
import ftplib
import os
import config
from PIL import Image


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
    time.sleep(10) #warmup

    for filename in camera.capture_continuous('images/image{counter:05d}.jpg'):
        print('Captured %s' % filename)
        aws_upload_image(filename)
        im = Image.open(filename)
        im.rotate(180)
        im.save(filename)
        im.close()
        print("file rotated and saved")
        aws_upload_image(filename)
        os.remove(filename)
        time.sleep(60 * 60) # wait 1 hour
        

