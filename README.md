*disclamer : keep a save of your file and check if everything is okay after using this program, it might broke some things*

*important : this program use NConvert which is included to help you using this script, nconvert is free for private non commercial or educationnal use, but paid otherwise, please check the license in the nconvert folder*

# LibreOffice Crop Fix

On old version of libreoffice, opening a file containing cropped image might result with glitched image.
When you crop a picture in libreoffice, the original file is keeped which allow you to change the crop later.
This python programme permanantly replace image with cropped image, which have for effect to fix the glitch.

# Usage
Download the software and drag & drop your odt file on the python file (you must have python installed).
This should create an `odt_fixed.odt` file. Open it, libreoffice should tell you the file is broken and ask you if you want to repair it.
Accept and save the repaired file.

# Privacy
Having libre office keep the uncropped file might be dangerous if the uncropped picture contain sensitive data.
By using this program to permanantly crop image, you can avoid that.
Normally, the odt_fixed.odt file should still have the uncropped file in it's data, but the uncropped file should be deleted after you let libreoffice repair the file.
