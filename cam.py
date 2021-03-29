import cv2
import imutils

cap = cv2.VideoCapture(0)


while(True):
  ret, frame = cap.read()
  frame = imutils.resize(frame, width=320)
  frame = cv2.flip(frame,180)
  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()