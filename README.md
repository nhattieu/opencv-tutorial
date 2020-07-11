`VI`
# OPENCV TUTORIAL

## Cài đặt

### 1. Python

> Cài đặt môi trường Python, ở đây là **Python 3**

```
https://www.python.org/downloads/
```

![setting-python-3](/assets/images/setting-python-3.png)


> Kiểm tra phiên bản **Python**

```
python --version
```
---

### 2. OpenCV

> Đầu tiên kiểm tra xem gói thư viên `pip`

```
pip --version
```

> Nếu chưa có thì cài đặt, thường thì cài đặt Python ở trên sẽ có gói `pip` này rồi

```
https://phoenixnap.com/kb/install-pip-windows
```

> Để update `pip`

```
python -m pip install --upgrade pip
```

> Sau khi kiểm tra `pip`, ta dùng lệnh

```
pip install opencv-python
```

> Cài đặt xong ta kiểm tra phiên bản `opencv` 

> Vì opencv chỉ hoạt động bằng lệnh trong **Python** nên ta phải dùng **Python**

> Thư viện được gọi tên là `cv2`

```
python
import cv2
cv2.__version__
```

![setting-check-opencv.png](/assets/images/setting-check-opencv.png)

---

## Cài xong rồu thì dứt thôu

Ở đây tạo thư mục tên `assets` để chứa các tài nguyên như hình ảnh `images`, video `videos`,.. để nhìn cho gọn thôi chứ không có giề.

### 1. Ngồi dọc với hình ảnh


```
import cv2

def write_img(src, des):

    img = cv2.imread(src, 0)
    cv2.imshow('Tieu de cua cai hinh nay ve 1 em gai xinh tuoi!', img)
    key = cv2.waitKey(0) & 0xFF

    # khi bam ESC thi no tat
    if key == 27:
        print('Gut bai! Tu bi con ti niu')
        cv2.destroyAllWindows()

    # bam 's' thi no luu lai
    elif key == ord('s'):
        cv2.imwrite(des, img)
        print('Gio hinh nay la cua taoooooooo')
        cv2.destroyAllWindows()

src = './assets/images/lena.jpg'
des = './assets/images/lena-copy.png'
write_img(src, des)
```

> Muốn sử dụng **opencv** thì phải `import` thư viện `cv2`

```
import cv2
```

> Đọc hình ảnh, ở đây có 2 parameter, nếu chỉ truyền đường dẫn không thôi thì mặc định là 1
> - 1 -     chỉ lấy màu của hình
> - 0 -     lấy mày xám
> - -1 -    lấy tất cả của hình ảnh

```
img = cv2.imread(src, 0)
```

> Hiển thị hình ảnh, gồm tiêu đề và hình ảnh đã đọc

```
cv2.imshow('Tieu de cua cai hinh nay ve 1 em gai xinh tuoi!', img)
```

> Gán thời gian chờ hiển thị hình ảnh, nếu `cv2.waitKey(0)` chứa tham số là 0 thì thời gian chờ sẽ là vô hạn, còn không thì sẽ tính theo milisecond. Hết thời gian chờ thì flame sẽ bị destroy.

> 0xFF là 1 dãy số 8 bits để xác định đuôi, cái này chưa rõ lắm

```
key = cv2.waitKey(0) & 0xFF
```

> Lệnh `cv2.waitKey(0)` sẽ chờ khi bấm phím `ESC` để dừng frame

> Lệnh `cv2.destroyAllWindows` để giải phóng tất cả frame đang dùng, đối với chương trình nhỏ thì không dùng cũng được

```
    if key == 27:
        print('Gut bai! Tu bi con ti niu')
        cv2.destroyAllWindows()
```

> Lệnh `cv2.waitKey()` sẽ chờ khi bấm phím `s` thì lưu lại hình ảnh

> Lệnh `cv2.imwrite(des, img)` Ghi hình ảnh vào 1 file mới

```
    elif key == ord('s'):
        cv2.imwrite(des, img)
        print('Gio hinh nay la cua taoooooooo')
        cv2.destroyAllWindows()
```

> Nguồn khảm khảo

```
https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/
https://www.geeksforgeeks.org/python-opencv-cv2-imwrite-method/
```