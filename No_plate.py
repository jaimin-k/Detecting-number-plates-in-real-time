import cv2
frameWidth = 640
frameHeight = 480
nplatecascade = cv2.CascadeClassifier("CV/haarcascade_russian_plate_number.xml")
minArea = 200
color = (255,0,255)
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

while True:
    succ,img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nplate = nplatecascade.detectMultiScale(imgGray,1.1,20)
    for(x, y, w, h) in nplate:
        area=w*h
        if area > minArea:
            cv2.rectangle(img,(x,y),(x+2,y+h),(255,0,255),2)
            cv2.putText(img, "Number_Plate",(x+2,y+2),cv2.FONT_HERSHEY_PLAIN,1,(0,100,98),1)
              
            imgRoi = img[y:y+h,x:x+w]
    
            cv2.imshow("ROI",imgRoi)


    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break