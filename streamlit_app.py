import streamlit as st
import cv2
import numpy as np
from hand_tracking import HandDetector

st.set_page_config(page_title="Gesture Control", layout="wide")

st.title("🧠 Gesture Control Dashboard")

st.sidebar.title("Controls")
st.sidebar.write("1 Finger → Volume")
st.sidebar.write("3 Fingers → Brightness")

run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])
mode_display = st.empty()
value_display = st.empty()

cap = cv2.VideoCapture(0)
detector = HandDetector()

mode = "Volume"

while run:
    success, img = cap.read()
    if not success:
        break

    img = detector.find_hands(img)
    lmList = detector.find_position(img)

    if len(lmList) != 0:

        x1, y1 = lmList[4][1:]
        x2, y2 = lmList[8][1:]

        length = np.hypot(x2 - x1, y2 - y1)
        value = int(np.interp(length, [20, 200], [0, 100]))

        # Finger detection
        fingers = []
        fingers.append(1 if lmList[8][2] < lmList[6][2] else 0)
        fingers.append(1 if lmList[12][2] < lmList[10][2] else 0)
        fingers.append(1 if lmList[16][2] < lmList[14][2] else 0)

        totalFingers = fingers.count(1)

        if totalFingers == 3:
            mode = "Brightness"
        elif totalFingers == 1:
            mode = "Volume"

        # Display only (NO system control)
        mode_display.metric("Mode", mode)
        value_display.metric("Value", f"{value}%")

        cv2.putText(img, f"{mode}: {value}%", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(img)

cap.release()