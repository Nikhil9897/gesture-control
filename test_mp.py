import mediapipe as mp

print("Mediapipe path:", mp.__file__)
print("Has solutions:", hasattr(mp, "solutions"))