import cv2

cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)

frame1 = cv2.imread("Figure_1.1.png")
frame3 = cv2.imread("Figure_3.png")

compare1 = cv2.compare(frame1,frame3,0)
compare2 = cv2.compare(frame1,frame3,0)

cv2.imshow('image1', compare1)
cv2.imshow('image2', compare2)

if compare1.all():
    print "equal"
else:
    print "not equal"

if compare2.all():
    print "equal"
else:
    print "not equal"

cv2.waitKey(0)
cv2.destroyAllWindows()
