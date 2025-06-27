import cv2
import torch
import pygame
from ultralytics import YOLO

# Load the trained YOLOv8 model
model_path = "C:/Users/Aravazhi Chezhian/Desktop/Testing/best.pt"  # Update with your model path
model = YOLO(model_path)

# Initialize pygame mixer for playing sound
pygame.mixer.init()
# Use double backslashes OR a raw string (r"")
alert_sound = r"C:\Users\Aravazhi Chezhian\Desktop\lava\alert.wav"


# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run YOLO model on the frame
    results = model(frame)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            confidence = float(box.conf[0])  # Confidence score
            class_id = int(box.cls[0])  # Class index
            class_name = model.names[class_id]  # Get class name

            # Draw bounding box and label
            label = f"{class_name}: {confidence:.2f}"
            color = (0, 255, 0)  # Green box for detected objects
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Play alert sound if a weapon is detected
            if class_name.lower() in ["gun", "knife"]:  # Modify class names if needed
                print("⚠️ Weapon Detected:", class_name, "Confidence:", confidence)
                pygame.mixer.Sound(alert_sound).play()

    # Display output
    cv2.imshow("YOLOv8 Real-Time Detection", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
