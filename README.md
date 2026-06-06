# DSClass_FaceLogin
the Project of Logging on your own PC using your face

📂 Repository Structure
You should organize your template repository with the following files:
<pre>
├── .github/
│   └── workflows/
│       └── classroom.log  # (Optional) For autograding setups
├── src/
│   ├── __init__.py
│   ├── main.py            # Application entry point & UI/loop
│   ├── detector.py        # Students implement MediaPipe Face Detection/Mesh
│   └── recognizer.py      # Students implement face embedding/matching
├── data/
│   └── known_faces/       # Directory to store authorized user reference images
│       └── anchor.jpg     # Placeholder target face
├── requirements.txt       # Project dependencies
└── README.md              # Project instructions and student documentation
</pre>

# Assignment: Face Recognition Based Login System using MediaPipe

## Objective
Your task is to build a secure, real-time local authentication system using Python, OpenCV, and the **MediaPipe** library. The system must process an active webcam stream, detect when a user is in front of the screen, and match their facial features against an authorized local profile directory to grant or deny access.

---

## Getting Started

### 1. Prerequisites & Installation
Ensure you have Python 3.9+ installed. Clone this repository and install the required library frameworks:
<pre>
```bash
pip install -r requirements.txt
</pre>

### 2. Setup Your Reference Profile

Before running the code, add a clear picture of your face to the authorized users directory:

    Save your image inside data/known_faces/

    Name the file with your name (e.g., john_doe.jpg). The system will parse the filename as the authorized user ID.

### 3. Tasks to Implement

You need to complete the following tasks marked with TODO in the source code:

#### Task Group A: Face Detection (src/detector.py)
1. Initialize the MediaPipe Pipeline: Configure the MediaPipe face solutions class with optimal parameters for real-time inference.
2. Frame Preprocessing: Correctly map the frame color space channels to meet MediaPipe's expectations.
3.Bounding Box Isolation: Parse the solution output to isolate coordinates for the primary face in the frame.

#### Task Group B: Verification Logic (src/recognizer.py)
4. Anchor Database Setup: Read images from data/known_faces/, extract reference markers, and index them into memory.
5. Distance Metrics: Implement a matching threshold metric (e.g., Euclidean distance or geometric landmark ratio matching) to verify if the active user matches the reference identity.

#### Task Group C: UI and States (src/main.py)
6. Visual Overlays: Render bounding boxes, feature tracking points, and state text directly onto the live OpenCV window.
7. System Authentication Actions: Design an access-granted state flow. (Optional enhancement: simulate triggering an OS login or locking mechanism when an unauthorized face stays active for too long).

### Running the Project

Run the application using:
<pre>
python src/main.py
</pre>

### Evaluation Criteria

* Accuracy: Does the system reliably authorize the registered profile and block unknown users?
* Edge-Case Resilience: How does the loop handle frames with missing faces, multiple users, or extreme angles?
* Code Quality: Adherence to functional clarity, documentation, clean separation of concerns, and efficient processing logic.
