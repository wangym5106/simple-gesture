from GestureDetection.GesturesApi import GestureProcessor
import cv2
import MouseApi

gp = GestureProcessor()
gp.bind("Horizontal Line Right to Left", lambda: MouseApi.scroll_up(1800))
gp.bind("Horizontal Line Left to Right", lambda: MouseApi.scroll_down(1800))
gp.bind("Vertical Line Top to Bottom", lambda: MouseApi.scroll_up(400))
gp.bind("Vertical Line Bottom to Top", lambda: MouseApi.scroll_down(400))

while True:
    gp.process()
    cv2.imshow('original', gp.original)
    cv2.imshow('thresholded', gp.thresholded)
    gp.draw()
    cv2.imshow('drawingCanvas', gp.drawingCanvas)
    k = cv2.waitKey(10)
    if k == 27:
        break
