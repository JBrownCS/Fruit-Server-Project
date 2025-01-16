#!/usr/bin/env python3

import requests
import os
import sys

# Upload the altered fruit images to the webserver

url = "http://localhost/upload/"

#establish current image directory for all images that need to be uploaded
current_img_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + 'supplier-data/images'                                                 

for imgfile in os.listdir(current_img_dir):
    current_img_path = os.path.join(current_img_dir, imgfile)
    current_img_name = os.path.basename(imgfile)[:-5]

    #It is an image if the image name starts with 0, otherwise skip that file
    if current_img_name[0] != '0':
         continue
    else:
         with open(current_img_path, 'rb') as upFile: 
                r = requests.post(url, files={'file': upFile})