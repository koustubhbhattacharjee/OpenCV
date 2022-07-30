import cv2 as cv
#img=cv.imread('Photos\marko-brecic-n08SJtxUVFE-unsplash.jpg')


def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#capture =cv.VideoCapture('Videos/videoplayback.mp4')

#while True:
 #   isTrue,frame=capture.read()
  #  print(frame.shape[0])
   # frame_resized=rescaleFrame(frame,0.5)

    #cv.imshow('Video Resized',frame_resized)

    #if cv.waitKey(20) & 0xFF==ord('d'):
     #   break
#capture.release()