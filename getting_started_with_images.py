import cv2

def write_img(src, des):

    img = cv2.imread(src, 0) # -1: color, 0: gray, 1: unchange. Default: 1
    cv2.imshow('Tieu de cua cai hinh nay ve 1 em gai xinh tuoi!', img)
    key = cv2.waitKey(0) & 0xFF

    if key == 27:
        print('Gut bai! Tu bi con ti niu')
        cv2.destroyAllWindows()

    elif key == ord('s'):
        cv2.imwrite(des, img)
        print('Gio hinh nay la cua taoooooooo')
        cv2.destroyAllWindows()

src = './assets/images/lena.jpg'
des = './assets/images/lena-copy.png'
write_img(src, des)















