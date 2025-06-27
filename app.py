import cv2
import torch
import pygame
import threading
from flask import Flask, Response, render_template
from ultralytics import YOLO

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Load trained YOLOv8 model
model_path = r"C:\Users\Aravazhi Chezhian\Desktop\Testing\best.pt"  # Corrected path
model = YOLO(model_path)

# ✅ Initialize Pygame for sound alerts
pygame.mixer.init()
alert_sound = r"C:\Users\Aravazhi Chezhian\Desktop\lava\alert.wav"  # Corrected path

# ✅ Open Webcam
cap = cv2.VideoCapture(0)

def detect_objects():
    """Continuously detects weapons in real-time from webcam."""
    while True:
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
                
                # Draw bounding box & label
                label = f"{class_name}: {confidence:.2f}"
                color = (0, 0, 255) if class_name.lower() in ["gun", "knife"] else (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                # 🔴 Trigger alert if weapon detected
                if class_name.lower() in ["gun", "knife"]:  
                    print(f"⚠️ Weapon Detected: {class_name} | Confidence: {confidence:.2f}")
                    pygame.mixer.Sound(alert_sound).play()

        # Stream the frame
        _, buffer = cv2.imencode(".jpg", frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# ✅ Flask Route for Video Stream
@app.route('/video_feed')
def video_feed():
    return Response(detect_objects(), mimetype='multipart/x-mixed-replace; boundary=frame')

# ✅ Flask Route for Home Page
@app.route('/')
def index():
    return render_template('index.html')

# ✅ Start the Flask App
if __name__ == '__main__':
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)).start()

    # Keep running webcam detection
    detect_objects()
