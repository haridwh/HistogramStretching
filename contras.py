import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc

def showImage(image, imageN):
    plt.figure()
    plt.title('Before')
    plt.imshow(image, cmap=plt.cm.gray)
    plt.figure()
    plt.title('After')
    plt.imshow(imageN, cmap=plt.cm.gray)
    plt.show()

def normalisasi(image):
    h = np.histogram(image, bins=np.arange(257))[0]
    H = np.cumsum(h)
    H_m = np.ma.masked_equal(H,0)
    H_m = (120/float((H_m.max()-H_m.min())/float(2)))*H_m
    h = np.ma.filled(H_m,0).astype('uint8')
    img_m = h[image]
    return img_m

def main():
    img = misc.imread(sys.argv[1])
    filename = sys.argv[1].split('.',1)[0]
    normImg = normalisasi(img)
    showImage(img ,normImg)
    misc.imsave(filename+'Norm.jpg',normImg)

if __name__ == "__main__":
    main()
