from ultralytics import YOLO
import numpy as np
import cv2

#load video
video_path = "test_video/traffic-sign-to-test.mp4"
capture = cv2.VideoCapture(video_path)

#load custome model
model = YOLO("traffic_sign.pt")
count = 0

while True:
    ret, frame = capture.read()
    if not ret:
        break

    count += 1
    if count % 3 != 0:
        continue

    results = model(frame)
    for result in results:
        bbox = result.boxes

    for box in bbox:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,255),3)

    cv2.imshow("video", frame)
    key = cv2.waitKey(1)
    if key == 27:  # esc key
        break

capture.release()
cv2.destroyAllWindows()
