import cv2



facecase = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

image = cv2.imread("C:/Users/User/Desktop/face.jpg")


faces = facecase.detectMultiScale(image,scaleFactor=1.1,minNeighbors=5,minSize=(10,10),flags = cv2.CASCADE_SCALE_IMAGE)

imghigh = image.shape[0]
imgwideth = image.shape[1]

cv2.rectangle(image,(10,imghigh-10),(110,imghigh),(0,0,0),-1)
cv2.putText(image,"Find " + str(len(faces)) + " face", (10,imghigh-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(128.255,0),2)

cv2.namedWindow("facedetect")
cv2.imshow("facedetect",image)
cv2.waitKey()
cv2.destroyAllWindows()