import cv2
capture = cv2.VideoCapture('/home/bor/embedded_project_ML/test3_4.mp4')
frameNr = 0
dims = (20,20)

while (True):
    success, frame = capture.read()
    if success:
        frame = cv2.resize(frame, dims, interpolation = cv2.INTER_AREA)	# resize img to fit dims
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'/home/bor/embedded_project_ML/Dataset/Training/4/test3_{frameNr}.jpg', frame)
    else:
        break
    frameNr = frameNr+1
capture.release()


