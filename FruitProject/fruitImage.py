
'''
Read all the images from the images folder and convert them from 
30002000 .tiff files to 600x400 jpg files
'''

import os
import sys
from PIL import Image


#establish current image directory for all images that need to be updated
current_img_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + 'supplier-data/images'


#Loop through directory and update images
for imgfile in os.listdir(current_img_dir):

    #Find image path and image name
    curr_img_path = os.path.join(current_img_dir, imgfile)
    curr_img_name = os.path.basename(imgfile)[:-5]
    
    #It is an image if the image name starts with a 0, otherwise skip that file
    if curr_img_name[0] != "0":
        continue
    else:
        #Open the image and format it correctly
        with Image.open(curr_img_path) as image:
            #Convert image to RGB so it can be formatted to JPG, then rotate and resize
            new_img = image.convert('RGB')
            new_img = new_img.resize((600,400))
            new_img_path = current_img_dir + curr_img_name + '.jpeg'
            

            new_img.save(new_img_path, 'JPEG')
            print(new_img.format, new_img.size)
        #Remove the old versions of the images
        os.remove(curr_img_path)
        
