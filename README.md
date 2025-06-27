# VISION-GUARD---a-real-time-AI-based-weapon-detection-system
VISION GUARD is a real-time AI-based system that detects weapons in live video using YOLOv8, with alerts, notifications, and live monitoring.
# 🔒 VISION GUARD – Real-Time AI-Based Weapon Detection System

**VISION GUARD** is a real-time AI-powered weapon detection system that uses deep learning and computer vision to automatically identify dangerous weapons—such as **guns and knives**—in live CCTV footage. Designed to enhance public safety and reduce reliance on manual surveillance, the system delivers instant alerts and real-time monitoring to improve threat response times.

---

## 🧠 Why VISION GUARD?

Traditional CCTV systems are limited by human monitoring, which is vulnerable to fatigue and delayed responses. **VISION GUARD** solves this problem using intelligent automation:

- ✅ Real-time weapon detection using **YOLOv8**
- ✅ Instant alerts via sound and push notifications
- ✅ Real-time live dashboard for remote monitoring
- ✅ Automatic evidence storage in Google Drive

---

## 🚀 Key Features

### 🔍 YOLOv8-Based Weapon Detection
- High-speed object detection using Ultralytics YOLOv8
- Trained on custom dataset with `gun` and `knife` classes
- Draws bounding boxes and confidence scores in live video

### 📢 Immediate Local Alerts
- Uses **Pygame** to trigger a loud alarm upon detection
- Alerts people nearby for rapid awareness

### 📲 Push Notifications via ntfy.sh
- Sends real-time notifications to security personnel
- Works on mobile or desktop via ntfy.sh subscriptions

### ☁️ Secure Google Drive Logging
- Saves frames with detected weapons to Google Drive
- Useful for documentation and forensic evidence

### 🌐 Flask-Based Web Dashboard
- Live video stream with detection overlays
- Accessible from any browser or network device

---

## ⚙️ Tech Stack

| Component        | Technology             |
|------------------|-------------------------|
| Object Detection | YOLOv8 (Ultralytics)    |
| Model Training   | Google Colab (GPU)      |
| Backend Server   | Flask                   |
| Notifications    | ntfy.sh                 |
| Audio Alerts     | Pygame                  |
| Evidence Storage | Google Drive API        |
| Dashboard        | HTML, CSS (Flask View)  |

---

## 🏗️ System Architecture

1. CCTV/Live Video Feed  
2. YOLOv8 Model detects weapons  
3. Flask server streams video  
4. Pygame triggers audio alert  
5. ntfy.sh sends push notifications  
6. Detected frames saved to Google Drive

---

## 🖥️ Deployment

### 🔧 Model Training
- Train YOLOv8 model in **Google Colab** using custom dataset (gun/knife)
- Export best `.pt` model weights

### 🌐 App Deployment
- Integrate YOLOv8 model with Flask
- Run Flask server locally or on cloud
- Stream video using OpenCV

---

## 📍 Use Cases

- 🚉 Public transportation (stations, airports)
- 🏫 Schools, colleges, and universities
- 🛒 Shopping malls and commercial spaces
- 🏛 Government and corporate buildings
- 🏙 Smart city surveillance networks

---

## 🛡 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Vishnu K E**  
📧 [vishnuke3@gmail.com](mailto:vishnuke3@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/vishnu-k-e-53abbb25b/)

---

## 📌 Tags

#YOLOv8 #WeaponDetection #ComputerVision #DeepLearning #AI #Surveillance #Flask #RealTimeDetection #PublicSafety #SmartCity #Python #ntfy #GoogleColab #OpenCV #SecuritySystem

![image](https://github.com/user-attachments/assets/102df664-bcbf-4ddd-8bce-3a4ec3ab8317)
![image](https://github.com/user-attachments/assets/7bd4fc9c-cbdc-4b5e-a4c3-aa5f6016ab9c)
![image](https://github.com/user-attachments/assets/39b712db-4d00-4535-8172-7584098f9ffc)
![image](https://github.com/user-attachments/assets/de53eaa9-6352-43fb-afae-84fbd231ab01)
![image](https://github.com/user-attachments/assets/ca121d33-3229-4990-9c2f-8b444a93b17d)
![image](https://github.com/user-attachments/assets/cc951a86-661b-4ab7-94bc-cc52a601c1f0)
