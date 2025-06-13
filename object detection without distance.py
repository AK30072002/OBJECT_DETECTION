from picamera2 import Picamera2
import time
import cv2
from ultralytics import YOLO
model =YOLO("pendrive.pt")
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640,480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()
time.sleep(2)

while True:
	frame = picam2.capture_array()

	results = model.predict(source=frame, conf=0.7, verbose=False)

	annotated_frame = results[0].plot()

	cv2.imshow("YOLOv8 Detection", annotated_frame)

	if cv2.waitKey(1) & 0xFF == ord("q"):
	   break

cv2.destroyAllWindows()
