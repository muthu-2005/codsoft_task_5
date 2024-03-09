import cv2
traineddataset=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('ind.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
faces=traineddataset.detectMultiScale(gray)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(105,255,0),2)
cv2.imshow('Face_detect',img)
cv2.waitKey()


