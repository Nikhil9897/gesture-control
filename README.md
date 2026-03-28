# 🧠 Hand Gesture Controlled System for Contactless Device Interaction

## 📌 Overview

This project is a real-time computer vision system that enables users to control system functions such as **volume and brightness** using hand gestures. It uses **OpenCV** and **MediaPipe** for hand tracking and gesture recognition, providing a touchless and interactive user experience.

---

## 🚀 Features

* ✋ Real-time hand detection using webcam
* 🎯 Finger tracking and gesture recognition
* 🔊 Volume control using finger distance
* 💡 Brightness control (with system compatibility)
* 🔄 Mode switching using gestures
* 🎚️ Smooth and stable control system
* 📸 Screenshot capture feature
* ⚡ FPS display and performance tracking
* 🎨 Clean and interactive UI overlay

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy
* Pycaw (for volume control)
* Screen Brightness Control

---

## 📂 Project Structure

gesture-control/
│
├── app.py                # Main application (run this)
├── hand_tracking.py      # Hand detection module
├── streamlit_app.py      # Optional UI dashboard
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Nikhil9897/gesture-control.git
cd gesture-control
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

### 3️⃣ Activate environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

▶️ How to Run the Project
🔥 Main Application (Recommended)
python app.py

The project is fully executable via the command line using python app.py, without requiring any GUI-based setup, ensuring compatibility with automated evaluation environments.

🎨 Optional Streamlit UI (Visualization Only)
streamlit run streamlit_app.py

Note: The Streamlit interface is provided for visualization purposes. The core system control (volume and brightness) is implemented in the OpenCV application (app.py) for better real-time performance.

## 🖐️ Gesture Controls

| Gesture            | Function                |
| ------------------ | ----------------------- |
| ☝️ One finger      | Volume control mode     |
| 🤟 Three fingers   | Brightness control mode |
| 🤏 Finger distance | Adjust value            |

---

## 🎮 Controls

* Move fingers → Adjust volume/brightness
* Press **S** → Capture screenshot
* Press **ESC / Q** → Exit application

---

## ⚠️ Notes

* Brightness control may not work on all systems (depends on hardware support).
* For best performance, use the **OpenCV application (`app.py`)** instead of Streamlit.
* Streamlit UI is included for demonstration purposes only.

---

## 📊 Future Improvements

* Add mouse control using gestures
* Add media playback control (play/pause)
* Improve UI with advanced frontend frameworks
* Add gesture-based shortcuts

---

## 🧑‍💻 Author

Developed as part of a Computer Vision course project.

---

## 📄 License

This project is for academic and educational purposes only.
