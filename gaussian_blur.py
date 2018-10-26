from PIL import Image
from math import pi, log, exp
import numpy as np
import math

def blur_py(img, r):
    q=r*0.38
    s=0
    w, h = img.size
    a = np.array(img.getdata(), dtype=np.uint8).reshape(h, w)
    b = np.zeros((h,w), dtype=np.uint8)
    g = np.zeros((r*2+1,r*2+1))
    k = np.zeros((r*2+1,r*2+1))
    for y in range(-r,r+1):
        for x in range(-r,r+1):
            g[y+r,x+r]=1.0/(2.0*pi*q*q)*exp(-((x)*(x)+(y)*(y))/(2.0*q*q))
            s+=g[y+r,x+r]
    k=g/s
    for i in range(r+1,h-r):
        for l in range(r+1,w-r):
             b[i,l]=np.sum(a[i-r:i+r+1,l-r:l+r+1]*k)
                
    print (k)
    print ("a=",a)
    print ("b=",b)
    return Image.fromarray(b)

img = Image.open('darwin.png')
img.load()

print("Image size is", img.size)
print("Image mode is", img.mode)

print("getdata[1]=", img.getdata()[1])
a = np.array(img, dtype=np.uint8).reshape(img.size[::-1])
print("a[0,1]=", a[0,1])
b = a[100:3000, 100:3000]
pic = Image.fromarray(b)

blur_py(pic,3).show()