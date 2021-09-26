import cv2
import numpy as np
import matplotlib.pyplot as plt
import  glob
import tkinter as tk
from tkinter import filedialog

def select_img():
    root = Tkinter.Tk()
    root.withdraw()

    file_path = tkFileDialog.askopenfilename()
    return file_path

def  show_img(img):
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.show()

def show_img_in_openCV(img):
    #第一個為視窗名稱
    cv2.imshow("myimg",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def take_img_from_webcam() :
    cap = cv2.VideoCapture(0)        #開啟攝像頭
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
    return "C:/Users/User/Desktop/test.png"

def crop_img(img):
    # 裁切區域的 x 與 y 座標（左上角）
    x = 100
    y = 100

    # 裁切區域的長度與寬度
    w = 250
    h = 150

    # 裁切圖片
    crop_img = img[y:y+h, x:x+w]
    return crop_img

def process_img(img):
    img = crop_img(img)
    return img

if __name__ == '__main__':
    print("if yot want to use webcam to select picture insert number 1")
    print("if you want to select picture in your computer insert number2")
    num = int(input())
    if num == 1:
        file_name = take_img_from_webcam()
    elif num == 2:
        file_name = select_img()

    origin_img = cv2.imread(file_name)
    show_img_in_openCV(origin_img)
    show_img(origin_img)

    result_img = process_img(origin_img)
    show_img_in_openCV(result_img)

    cv2.imwrite("C:/Users/User/Desktop/result_Dog.jpg", result_img)
