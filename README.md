# 🖐️ Hand Gesture Virtual Mouse (Like Apple Vision Pro – but with Python!)

Control your computer using just your **hands in the air** — no hardware, no headset.  
This project uses a webcam to turn hand gestures into **mouse movement, clicks, and scrolling**.

Inspired by the gesture system in **Apple Vision Pro**, but powered entirely by **Python + OpenCV + MediaPipe**.

---

## 🚀 Features

✅ **Air Mouse** – Move your index finger and your mouse follows  
✅ **Left Click** – Pinch your index and thumb together  
✅ **Scroll** – Pinch index and middle finger, then move up/down to scroll  
✅ **Click Cooldown** – 3 second delay after click to avoid accidental spamming  
✅ **Real-time Webcam Input**  
✅ **No extra hardware required**

---

## 🧠 Tech Stack

- [MediaPipe](https://github.com/google/mediapipe) – Real-time hand landmark tracking  
- [OpenCV](https://opencv.org/) – Video capture & frame drawing  
- [PyAutoGUI](https://pyautogui.readthedocs.io/) – Mouse control in Python  
- [Python](https://www.python.org/) – Because Python is magic 🐍

---

## 🛠️ Installation

```bash
pip install opencv-python mediapipe pyautogui
```

## ▶️ How to Use
1. Clone this repo or download the script 
2. Run the script:
```bash
python gesture_mouse.py
```
3. Allow camera access
4. Use your hand to control:

## ✋ Gesture Controls:


Index finger moves - Move mouse

Index + Thumb pinch - Left click

Index + Middle pinch + up/down - Scroll page

## 🧠 Future Ideas

✌️ Right-click with index + ring finger

🖐️ Drag gesture with pinch hold

🔊 Volume control with palm distance

💬 Voice + gesture combo commands

##  Credits
Made by Rohith Reddy — inspired by Apple Vision Pro and open-source love 💙