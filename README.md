# Fruit-Server-Project

Problem Statement:
You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

Here are the scripts I created for this project:
1) fruitImage.py for altering the .tif files to jpeg
2) fruitImageUpload.py for uploading the updated images to the web service via the POST method
3) fruitDescriptionUpload.py for reading all the description .txt files and posting each fruit description with its corresponding image to the web service. I provided an example picture using Google's images, but I provided my own for testing. I have a image_original folder so the original images are still kept intact.
4) reports.py for gathering all the fruit names and weights and generating a pdf file with that information. The end result is in the tmp folder
5) emails.py file for generating emails for the reports and health checks
6) healthchecks.py to perform all system health checks such as if CPU usage is above 80%, Available disk space is lower than 20%, Available memory is less than 100MB and the hostname "localhost" cannot be resolved to "127.0.0.1"

This was the Final Project for the Google IT Automation with Python Course.
