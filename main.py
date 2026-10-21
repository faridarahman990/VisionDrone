
import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    raise SystemExit

print("VisionDrone camera test started.")
print("Press Q to exit.")

while True:
    success, frame = cap.read()

    if not success:
        print("Error: Could not read a camera frame.")
        break

    cv2.imshow("VisionDrone - Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
