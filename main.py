import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time
cap=cv2.VideoCapture(1)
cap.set(3,1080)
cap.set(4,720)

detector=HandDetector(detectionCon=0.8)

Vill=cv2.imread("Villain2.png",cv2.IMREAD_UNCHANGED)
fire1=cv2.imread("fire.jpg",cv2.IMREAD_UNCHANGED)
fire2=cv2.imread("fire.jpg",cv2.IMREAD_UNCHANGED)
fire3=cv2.imread("fire.jpg",cv2.IMREAD_UNCHANGED)
burst=cv2.imread("burst2.png",cv2.IMREAD_UNCHANGED)
print(burst.shape)
oy,ox=10,980
fy1,fx1=50,10

flag=False
score=0
start_time=None
while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img,flipType=False)
    if flag:
      img=burst
      cvzone.putTextRect(img,"Game Over",[250,600],scale=5,thickness=5,offset=10)    
      cvzone.putTextRect(img,f"Score={score}%",[130,700],scale=5,thickness=5,offset=10)
    else:
         fh,fw,_=fire1.shape
         if hands:
            if start_time==None:
               start_time=time.time()
            lmList=hands[0]['lmList']
            cursor=lmList[8]
            if fx1<cursor[0]<fx1+fw and fy1<cursor[1]<fy1+fh:
               fx1,fy1=abs(cursor[0]-fw//2),abs(cursor[1]-fh//2)
            
         cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
         h,w,_=Vill.shape
         try:
            if not flag:
               img=cvzone.overlayPNG(img,Vill,[ox,oy])
               img[fy1:fy1+fh,fx1:fx1+fw]=fire1
               
         except:
            fx1=10
            fy1=50
         # Collision detection
         if fx1>ox and fx1<ox+w and fy1>oy and fy1<oy+h:
            end_time=time.time()
            score=((15/(end_time-start_time))*100)
            score=round(score,2)
            flag=True

    cv2.imshow("window",img)
    cv2.waitKey(1)