from GestureDetection.GesturesApi import GestureProcessor
import cv2

gp = GestureProcessor()

while True:
    gp.process()
    cv2.imshow('original', gp.original)
    cv2.imshow('thresholded', gp.thresholded)
    gp.draw()
    cv2.imshow('drawingCanvas', gp.drawingCanvas)
    k = cv2.waitKey(10)
    if k == 27:
        break
