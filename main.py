import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(1)
cap.set(3,1080)
cap.set(4,720)

detector=HandDetector(detectionCon=0.8)

Vill=cv2.imread("Villain.png")
fire=cv2.imread("fireball.png")

oy,ox=10,960
fy1,fx1=50,10
fy2,fx2=250,10
fy3,fx3=450,10
while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img,flipType=False)
    
    fh,fw,_=fire.shape
    if hands:
        lmList=hands[0]['lmList']
        length,info,img=detector.findDistance(lmList[8],lmList[12],img)
        
        if length<60:
            
            cursor=lmList[8]
            if fy1<cursor[0]<fy1+fh and fx1<cursor[1]<fx1+fw:
               fx1,fy1=cursor[0]-fw//2,cursor[1]-fh//2

    
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    h,w,_=Vill.shape
    
    img[oy:oy+h,ox:ox+w]=Vill
    img[fy1:fy1+fh,fx1:fx1+fw]=fire
    img[fy2:fy2+fh,fx2:fx2+fw]=fire
    img[fy3:fy3+fh,fx3:fx3+fw]=fire
    cv2.imshow("window",img)
    cv2.waitKey(1)