import cv2
from deepface import DeepFace

# Start video capture (0 = default webcam)
cap = cv2.VideoCapture(0)

print("Starting emotion detection... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB (DeepFace expects RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    try:
        # Analyze emotions
        result = DeepFace.analyze(rgb_frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']

        # Draw text on frame
        cv2.putText(frame, f"Emotion: {emotion}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    except Exception as e:
        # If face not detected or any error
        cv2.putText(frame, "No face detected", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show frame
    cv2.imshow('Real-Time Emotion Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close window
cap.release()
cv2.destroyAllWindows()
