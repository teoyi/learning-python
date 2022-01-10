import cv2 
import os 

print(os.getcwd())
os.chdir("/Users/luke/Desktop/Python/GitClone/webcam-motion-detector/practice/Files-2")

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.05,
minNeighbors = 5)

for x, y, w, h in faces: 
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
    # first one is image, then starting point of the rectangle
    # , then the other corner of the image, then color, then width of line

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

# print(faces)
# print(type(faces))

cv2.imshow("gray img", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
