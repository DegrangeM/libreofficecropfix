*disclamer : this might not work, I used this program i created to fix one of my file and share it because it might be usefull for someone else but it might not work for all file, so be carefull when using it*

# libreofficepermacropfix

When you crop a picture in libreoffice, it keep the original file which might be dangerous if the uncropped picture contain sensitive data.
This python programme permanantly crop the picture by cropping picture using nconvert and using it instead.

Also, cropped image create strange image glitch on old version of libreoffice so this might fix some files.


How to use :
Unzip your odt file, put the python program inside it. Download nconvert and change the location of nconvert in the python file. Run the program. Replace content.xml with contentfixed.xml. Go in Pictures Folder and delete sensitive image. Zip all file (be sure they are at the root of the zip file) and rename it to an odt. Open the odt, let libreoffice fix the file.
