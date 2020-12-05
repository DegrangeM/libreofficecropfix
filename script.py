import os
from PIL import Image
import re

imagesdir = os.listdir("Pictures/");

images = {}

for f in imagesdir :
    im = Image.open('Pictures/' + f);
    images['Pictures/' + f] = im.size # w,h
    
    
content = open("content.xml", "r", encoding="utf8").read()

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
    cmd = r"D:\Téléchargement\NConvert-win64\NConvert\nconvert.exe -crop " + str(pl) +" " + str(pt) + " " + str(pw) + " " + str(ph) + " -o Pictures/" + i[0] + ".png " + i[3]
    print(cmd)
    os.system(cmd)
    
content = re.sub(r'(<draw:frame draw:style-name="([^"]+)" .*? svg:width="[0-9.]+cm" svg:height="[0-9.]+cm" [^>]*><draw:image xlink:href=")[^"]+(" [^>]*></draw:frame>)',r"\1Pictures/\2.png\3",content)

open("contentfixed2.xml", "x", encoding="utf8").write(content)


content = re.sub(r'(<style:style style:name="[^"]+" [^>]+><style:graphic-properties [^>]*? fo:clip=")rect\(-?[0-9.]+cm, -?[0-9.]+cm, -?[0-9.]+cm, -?[0-9.]+cm\)"',r'\1rect(0cm, 0cm, 0cm, 0cm)"',content)

open("contentfixed3.xml", "x", encoding="utf8").write(content)
    
#print(style)
#print(img)
