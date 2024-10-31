import cv2
cap = cv2.VideoCapture(0)

'''list_example = [0, 1, 2, 3]
print(list_example[1:3])

exit()'''

while True:
    ret, frame = cap.read()
    height, wigth, _ = frame.shape
    frame[height//2-50:height//2+50, wigth//2-50:wigth//2+50] = frame[:100, wigth - 100:] = frame[:100, :100] = frame[height - 100:, wigth - 100:] = frame[height - 100:, :100] = [0, 0, 0]
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1000)
    if key == ord(' '):
        break

cv2.destroyAllWindows()
cap.release()
