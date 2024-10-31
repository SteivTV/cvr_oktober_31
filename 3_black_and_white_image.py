import cv2
import time



cap = cv2.VideoCapture(0) #номер вебкамеры, либо название камеры

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

FPS = 0
time_start =  time.time() # timestamp с 1970 года
print(time_start)

out = cv2.VideoWriter('Video.avi', cv2.VideoWriter_fourcc('N', 'J', 'P', 'G'),70, (frame_width, frame_height))

#T = time.time() - time_start
print(frame_width, frame_height)
#print(ord(' '))
while True:
    ret, frame = cap.read() #frame массив, ret возвращение return
    if not ret:
        continue
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(gray)
    cv2.imshow('Video_2', gray)
    k = cv2.waitKey(10) # миллисекунды ожидает нажатие клавиши
    if k == ord(' '):
        break
    FPS = round(1 / (time.time() - time_start))
    print(FPS)
    time_start = time.time()

out.release()
cap.release()
