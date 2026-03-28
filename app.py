import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import warnings
warnings.filterwarnings("ignore")

import cv2
import numpy as np
import time
from hand_tracking import HandDetector

# Volume control
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Brightness control
import screen_brightness_control as sbc

# ------------------ SETUP ------------------

# Volume setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[:2]

# Camera
cap = cv2.VideoCapture(0)
detector = HandDetector()

pTime = 0
smooth_val = 0
mode = "Volume"

# ------------------ MAIN LOOP ------------------

while True:
    success, img = cap.read()
    if not success:
        break

    img = detector.find_hands(img)
    lmList = detector.find_position(img)

    if len(lmList) != 0:

        # Thumb & Index
        x1, y1 = lmList[4][1:]
        x2, y2 = lmList[8][1:]

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), -1)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), -1)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        length = np.hypot(x2 - x1, y2 - y1)

        # ------------------ MODE SWITCH ------------------
        fingers = []

        fingers.append(1 if lmList[8][2] < lmList[6][2] else 0)
        fingers.append(1 if lmList[12][2] < lmList[10][2] else 0)
        fingers.append(1 if lmList[16][2] < lmList[14][2] else 0)

        totalFingers = fingers.count(1)

        if totalFingers == 3:
            mode = "Brightness"
        elif totalFingers == 1:
            mode = "Volume"

        # ------------------ CONTROL ------------------

        value = np.interp(length, [20, 200], [0, 100])

        if mode == "Volume":
            target = np.interp(length, [20, 200], [volMin, volMax])
            smooth_val += (target - smooth_val) * 0.2
            volume.SetMasterVolumeLevel(smooth_val, None)

        elif mode == "Brightness":
            try:
                current = sbc.get_brightness(display=0)[0]
                new_val = int(value)

                if abs(current - new_val) > 5:  # reduce flicker
                    sbc.set_brightness(new_val)

            except:
                # fallback (if brightness not supported)
                cv2.putText(img, "Brightness not supported",
                            (200, 150), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (0, 0, 255), 2)

        # ------------------ UI ------------------

        volBar = np.interp(length, [20, 200], [400, 150])
        percent = int(value)

        color = (0, int(255 * (percent/100)), int(255 * (1 - percent/100)))

        cv2.rectangle(img, (50, 150), (85, 400), (255, 255, 255), 2)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), color, -1)

        cv2.putText(img, f'{percent} %', (40, 450),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

        cv2.putText(img, f'Mode: {mode}', (250, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.putText(img, "Gesture Control System", (200, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Gesture Control", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        filename = f"screenshot_{int(time.time())}.png"
        cv2.imwrite(filename, img)
        print(f"Saved: {filename}")

    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()