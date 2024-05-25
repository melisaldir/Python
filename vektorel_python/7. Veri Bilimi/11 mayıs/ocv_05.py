import cv2
cap= cv2.VideoCapture("videolar/ornek1.mp4")

while cap.isOpened():
    ret, tekGoruntu = cap.read()
    if ret == True:
        sonuc = cv2.transpose(tekGoruntu)
        cv2.imshow("Pencere1",tekGoruntu)
        cv2.imshow("Pencere2",sonuc)
        tus = cv2.waitKey(1)
        if tus == ord("q"): break
    else: break

cap.release()
cv2.destroyAllWindows()