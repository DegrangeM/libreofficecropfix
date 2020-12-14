import sys
import os
# from zipfile import ZipFile
import shutil # zip,  dir deletion
from PIL import Image
import re #regex
#from subprocess import PIPE, Popen #cmd
#import subprocess

#def cmdline(command):
#    process = Popen(
#        args=command,
#        stdout=PIPE,
#        shell=True
#    )
#    return process.communicate()[0]

# from time import sleep

# Gestion du drag & drop de fichier
if len(sys.argv) < 2 :
    print("Merci de drag&drop le fichier à corriger")
    os.system("pause")
    quit()

#print(sys.argv[1])
    
shutil.rmtree('temp_fix_odt/', ignore_errors=True)

if os.path.exists("odt_fixed.odt"):
    os.remove("odt_fixed.odt")


# Décompression du fichier odt
shutil.unpack_archive(sys.argv[1], "temp_fix_odt/", "zip")

# Correction
imagesdir = os.listdir("temp_fix_odt/Pictures/");

images = {}

for f in imagesdir :
    im = Image.open('temp_fix_odt/Pictures/' + f);
    images['Pictures/' + f] = im.size # w,h
    
    
contentfile = open("temp_fix_odt/content.xml", "r+", encoding="utf8")
content = contentfile.read()

open("temp_fix_odt/content_svg.xml", "w", encoding="utf8").write(content)


# ('id', 't', 'r', 'b', 'l')
style = re.findall(r'<style:style style:name="([^"]+)" [^>]+><style:graphic-properties [^>]*? fo:clip="rect\((-?[0-9.]+)cm, (-?[0-9.]+)cm, (-?[0-9.]+)cm, (-?[0-9.]+)cm\)"', content)

styles = {}

for s in style :
    styles[s[0]] = {'t':float(s[1]), 'r':float(s[2]), 'b':float(s[3]), 'l':float(s[4])}

# [('id', 'w', 'h', 'url'),...]
img = re.findall(r'<draw:frame draw:style-name="([^"]+)" .*? svg:width="([0-9.]+)cm" svg:height="([0-9.]+)cm" [^>]*><draw:image xlink:href="([^"]*)" [^>]*></draw:frame>',content)


for i in img :
    s = styles[i[0]]
    print(s)
    print(i)
    pl = round(s['l'] * 37.7953) #/float(i[1])*images[i[3]][0])
    pr = round(s['r'] * 37.7953) #/float(i[1])*images[i[3]][0])
    pt = round(s['t'] * 37.7953) #/float(i[2])*images[i[3]][1])
    pb = round(s['b'] * 37.7953) #/float(i[2])*images[i[3]][1])
    pw = images[i[3]][0] - pr - pl
    ph = images[i[3]][1] - pb - pt
    print(pl, pr, pt, pb, pw, ph)
    nc = os.path.abspath(r"NConvert/nconvert.exe")
    nci = os.path.abspath(r"temp_fix_odt/" + i[3])
    nco = os.path.abspath(r"temp_fix_odt/Pictures/" + i[0] + ".png")
    cmd = nc + " -crop " + str(pl) +" " + str(pt) + " " + str(pw) + " " + str(ph) + " -o " + nco + " " + nci;
    print(cmd)
    print(os.system(cmd))
    #print(cmdline(cmd))
    #try:
    #    print(subprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT))
    #except subprocess.CalledProcessError as e:
    #    raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    
content = re.sub(r'(<draw:frame draw:style-name="([^"]+)" .*? svg:width="[0-9.]+cm" svg:height="[0-9.]+cm" [^>]*><draw:image xlink:href=")[^"]+(" [^>]*></draw:frame>)',r"\1Pictures/\2.png\3",content)

content = re.sub(r'(<style:style style:name="[^"]+" [^>]+><style:graphic-properties [^>]*? fo:clip=")rect\(-?[0-9.]+cm, -?[0-9.]+cm, -?[0-9.]+cm, -?[0-9.]+cm\)"',r'\1rect(0cm, 0cm, 0cm, 0cm)"',content)

contentfile.seek(0)
contentfile.write(content)
contentfile.truncate()


# Recompression du fichier
shutil.make_archive("temp_fix_odt", 'zip', "temp_fix_odt/")
os.rename("temp_fix_odt.zip", "odt_fixed.odt")
#os.system("pause")

    # zf = ZipFile(sys.argv[1], 'r')
    # zf.extractall('temp/')
    # zf.close()
