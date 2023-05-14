import cv2 # import from library
vid = cv2.VideoCapture(0)  # 0 is the port number(default) and vediocapture is a class
while True: #infinite loop
    ret, frame = vid.read()  # from read can capture a frame
    image = cv2.putText(frame,'Welcome to Al Ml class',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(250,250,250),2,cv2.LINE_AA)
                                        # where (50,50) is coordinates
                                        # 1 is the font scale # (0,0,250) is the colour
                                        # cv2.FONT_HERSHEY_SIMPLEX is the font
                                        # frame is the captured image
                                        # 2 is the thickness and cv2.LINE_AA to show the image
    cv2.imshow('AL VIDEO',image) # AL VIDEO video name
    if cv2.waitKey(1) & 0xFF == ord("q"):   # for 1 macrosec and q is pressed
         break  # if pass is given then it continous(and window is closed by using q )
vid.release()
cv2.destroyAllWindows()
#mediapipe process only RGB image
#landmark has coordinates

