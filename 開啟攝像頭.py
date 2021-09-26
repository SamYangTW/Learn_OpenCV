import cv2
from matplotlib import pyplot as plt
import numpy as np


cap = cv2.VideoCapture(0)        #開啟攝像頭

def take_img() :
    while(1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)     #生成攝像頭視窗
    
        if cv2.waitKey(1) & 0xFF == ord('q'):   #如果按下q 就截圖儲存並退出
            cv2.imwrite("C:/Users/User/Desktop/test.png", frame)   #儲存路徑
            break

    cap.release()
    cv2.destroyAllWindows()
    show_img()
    

def show_img():
    print("顯示照片")
    img_bgr = cv2.imread('C:/Users/User/Desktop/test.png')
    # 將 BGR 圖片轉為 RGB 圖片
    img_rgb = img_bgr[:,:,::-1]
    plt.imshow(img_rgb)
    plt.show()

if __name__ == '__main__':
    print("擷取照片")
    take_img()
    