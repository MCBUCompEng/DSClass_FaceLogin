import cv2
from detector import FaceDetector
from recognizer import FaceRecognizer

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    # Initialize student modules
    detector = FaceDetector()
    recognizer = FaceRecognizer()
    
    print("Starting Face Recognition Login System...")
    print("Press 'q' to exit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Flip the frame horizontally for a natural mirror view
        frame = cv2.flip(frame, 1)

        # 1. Detect Face
        face_detected, bbox = detector.detect_face(frame)

        if face_detected:
            # 2. Draw Bounding Box (Visual feedback)
            # TODO: TASK 7 - Draw visual markers around the face
            
            # 3. Recognize Face
            identity = recognizer.verify_face(frame, bbox)
            
            # 4. Handle Authentication States
            if identity != "Unknown":
                status_text = f"Access Granted: {identity}"
                color = (0, 255, 0)  # Green
                # TODO: Optional - Trigger a simulated system login or function call here
            else:
                status_text = "Access Denied: Unknown User"
                color = (0, 0, 255)  # Red
        else:
            status_text = "No Face Detected"
            color = (255, 0, 0)  # Blue

        # Display status on the screen
        cv2.putText(frame, status_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow('Face Recognition Login System', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
