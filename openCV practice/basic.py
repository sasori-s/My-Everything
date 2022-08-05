import cv2
framewidth = 640
framewidth = 480
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, framewidth)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break