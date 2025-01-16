#Upload all the fruit descriptions to the directory

import json
import os
import sys
import requests


#establish current directory for all descriptions that need to be posted to the server
current_desc_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '/supplier-data/descriptions'

#list for all fruit posts
fruit_post_list = []

os.chdir(current_desc_dir)
#Loop through directory and collect post data
for file in os.listdir(current_desc_dir):

    #Read file
    desc_file_name = os.path.basename(file)[:-5]
    desc_file = open(file, 'r')
    desc_info = desc_file.readlines()

    '''
    Line 1 is the Fruit Name
    Line 2 is the fruit weight
    Line 3 is the description
    The image name is the name of the image with the corresponding number
    so 001.txt has image 001.jpeg
    '''
    fruit_post_list.append({
        "name" :desc_info[0].strip(),
        "weight":int(desc_info[1].replace("lbs","")),
        "description":desc_info[2].strip(),
        "image_name": desc_file_name + '.jpeg'})
    
    desc_file.close()

#upload the fruit posts to the web server
#Url is in format http://[external-IP-address]/fruits
#external IP may have to be changed since this listed one is only temporary
url = 'http://34.75.139.109/fruits/'
for fruit in fruit_post_list:
    print(fruit)
    r = requests.post(url, data=json.dumps(fruit))


