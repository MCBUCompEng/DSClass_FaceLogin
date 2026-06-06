import cv2
import mediapipe as mp
import numpy as np

class FaceDetector:
    def __init__(self, min_detection_confidence=0.5):
        """
        TODO: TASK 1 - Initialize MediaPipe Face Detection or Face Mesh.
        """
        self.mp_face_detection = mp.solutions.face_detection
        # Hint: Initialize the face detection model here
        self.detector = self.mp_face_detection.FaceDetection(
            min_detection_confidence=min_detection_confidence
        )

    def detect_face(self, frame):
        """
        Detects faces in the frame.
        
        Parameters:
            frame (numpy.ndarray): The input BGR image from the webcam.
            
        Returns:
            bool: True if a face is detected, False otherwise.
            bbox: Bounding box coordinates (x, y, w, h) or normalized landmarks.
        """
        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # TODO: TASK 2 - Process the frame using the MediaPipe detector
        results = self.detector.process(rgb_frame)
        
        # TODO: TASK 3 - Extract bounding box of the primary face
        # Check if any face is detected, extract coordinates, and return them.
        
        # Default fallback (Modify this)
        return False, None
