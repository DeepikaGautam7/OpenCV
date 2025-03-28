import cv2 as cv

img = cv.imread("img/cat.jpg")

reimg= cv.resize(img, (800, 600))

cv.imshow("OpenCV Image", reimg)

cv.waitKey(0)

cv.destroyAllWindows()
