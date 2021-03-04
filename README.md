# simple-wallpaper-slideshow

A python script to change desktop wallpaper autmatically after a given period of time. 

### made only for GNOME 

Just download the repo.
cd into the folder
and type the following in terminal:
```
chmod +x install.sh
./install.sh
```
Now edit the wallpaper_slideshow.py file to set the path of the wallpapers folder(line 16) and the time(line 13) after which the wallpaper should change

And thats it. you can type wallpaper_slideshow to run it and kill_ws to stop it

# Uninstallation

delete the repo folder and
```
sudo rm /bin/wallpaper_slideshow
sudo rm /bin/kill_ws
```
