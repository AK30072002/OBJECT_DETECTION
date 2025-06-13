from picamera2 import Picamera2
from ultralytics import YOLO
import cv2
import time
import smbus2

# ====================== YOLOv8 and Camera Setup ============================
model = YOLO("pendrive.pt")  # Load custom-trained YOLOv8 model

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()
time.sleep(2)  # Give camera time to warm up

# ====================== I2C Setup ==========================================
bus = smbus2.SMBus(1)  # I2C bus number on RPi or Jetson Nano
ARDUINO_ADDRESS = 0x08  # I2C slave address of Arduino
distance_cm = None  # Variable to store the last read distance

# ====================== Main Loop ==========================================
cv2.namedWindow("YOLOv8 + Distance", cv2.WINDOW_NORMAL)

while True:
    # 1. Capture image from Picamera2
    frame = picam2.capture_array()

    # 2. Read distance from Arduino via I2C
    try:
        raw = bus.read_i2c_block_data(ARDUINO_ADDRESS, 0, 2)  # Read 2 bytes
        distance_cm = raw[0] | (raw[1] << 8)  # Combine low + high bytes
    except OSError as e:
        print("I2C Error:", e)

    # 3. Run YOLOv8 object detection
    results = model.predict(source=frame, conf=0.7, verbose=False)
    annotated = results[0].plot()  # Annotated image with YOLO boxes + labels

    # 4. Add distance overlay to each detection box
    if distance_cm is not None and results[0].boxes is not None:
        for box in results[0].boxes.xyxy.cpu().numpy().astype(int):
            x1, y1, x2, y2 = box
            cv2.putText(
                annotated,
                f"{distance_cm} cm",
                (x1 + 5, y1 + 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 0),  # Cyan color
                2,
                cv2.LINE_AA,
            )

    # 5. Display the annotated frame
    cv2.imshow("YOLOv8 + Distance", annotated)

    # 6. Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ====================== Cleanup ============================================
picam2.stop()
cv2.destroyAllWindows()
