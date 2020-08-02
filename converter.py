import sys
import os
from PIL import Image

#Grap First and Second Argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#Check if converted folder exit,if not create one
if not os.path.exists(output_folder):
	os.makedirs(output_folder)


#Loop through the entire folder 
for filename in os.listdir(image_folder):
  img = Image.open(f'{image_folder}/{filename}')

#To split the name of images imagename format
  clean_name = os.path.splitext(filename)[0]
#save the image to new folder
  img.save(f'{output_folder}/{clean_name}.png','png')

print("All photos have been converted")