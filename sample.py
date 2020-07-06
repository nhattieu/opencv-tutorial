import cv2
import numpy as np

img = cv2.imread('lena.jpg', 0)
cv2.imshow('Tieu de cua cai hinh nay ve 1 em gai xinh tuoi!', img)
key = cv2.waitKey(0)
if key > -1:
    print(f'May vua nhan phim {key} dung khong? Ghe hem?')
if key == 27:
    print('Gut bai! Tu bi con ti niu')
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('lena_copy.jpg', img)
    print('Gio hinh nay la cua taoooooooo')
    cv2.destroyAllWindows()

print ("width: %d pixels"% (img.shape[1]))
print ("height: %d pixels" % (img.shape[0]))
print ("channels: %d channels" % (img.shape[0]))

print(img.shape)