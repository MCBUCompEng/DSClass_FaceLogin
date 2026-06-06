import cv2
import numpy as np
import os

class FaceRecognizer:
    def __init__(self, database_dir="data/known_faces"):
        self.database_dir = database_dir
        self.known_embeddings = {}
        self.load_known_faces()

    def load_known_faces(self):
        """
        Loads authorized faces from the database directory and computes their features.
        """
        if not os.path.exists(self.database_dir):
            os.makedirs(self.database_dir)
            
        # TODO: TASK 4 - Loop through the database directory, load images, 
        # and extract reference facial feature profiles/embeddings.
        pass

    def verify_face(self, current_frame, face_bbox):
        """
        Compares the detected face in the current frame against known faces.
        
        Parameters:
            current_frame (numpy.ndarray): Current webcam frame.
            face_bbox: Coordinates of the detected face.
            
        Returns:
            str: Identity of the matched user, or "Unknown".
        """
        # TODO: TASK 5 - Extract features from the current face region.
        # TODO: TASK 6 - Compare features against self.known_embeddings using a distance metric (e.g., L2 or Cosine).
        
        # Default fallback (Modify this)
        return "Unknown"
