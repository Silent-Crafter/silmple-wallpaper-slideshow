import os
import time

def image_only(files):
	imgs = []
	for file in files:
		if file.find('.png',-4) != -1 or file.find('.jpg',-4) != -1 or file.find('.jpeg',-5) != -1:
			imgs.append(file)

	return imgs

#time-interval for next image in seconds. default is 10 mins.
delay = 10*60

#path to the wallpapers' folder
path = '/path_to_wallpapers_folder'

#no. of files will also include files with other extensions besides image 
#so be carefull cause any other file will f*ck up the program
images = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))]

images = image_only(images)

no_of_files = len(images)

while(True):
	for counter in range(no_of_files):
		os.system(f'gsettings set org.gnome.desktop.background picture-uri \'{path}/{images[counter]}\'')
		time.sleep(delay)
