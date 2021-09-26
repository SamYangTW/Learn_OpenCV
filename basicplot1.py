import cv2

cv2.namedWindow("plot")

image = cv2.imread("Dog.jpg")
cv2.line(image,(50,50),(200,200),(255,0,0),2)
cv2.rectangle(image,(100,200),(180,300),(0,255,0),3)

cv2.imshow("plot",image)
cv2.waitKey()
cv2.destroyAllWindows()