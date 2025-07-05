# 📷 Motion Detector using OpenCV

A real-time motion detection system built in Python using OpenCV and basic image processing techniques. It captures video feed from your webcam, detects motion by comparing frames, and highlights moving objects using bounding boxes.

---

## 🚀 Features

- 📸 Real-time video capture using webcam  
- 🔍 Motion detection via frame differencing  
- 🧠 Automatic object counting and labeling  
- 📐 Adjustable detection sensitivity  
- 🖼️ Live display with status overlay  

---

## 🛠️ Technologies Used

- **Python 3**
- **OpenCV (`cv2`)** – for computer vision and image processing
- **imutils** – for simplifying OpenCV tasks
- **time** – for initializing camera delay

---

## 🧠 How It Works

1. **Camera Initialization** – waits 3 seconds for stabilization.
2. **Reference Frame** – first frame is stored and blurred.
3. **Frame Comparison** – each new frame is compared with the first.
4. **Image Processing**:
   - Convert to grayscale
   - Apply Gaussian blur to reduce noise
   - Calculate absolute difference
   - Threshold and dilate the image
5. **Contour Detection** – finds moving regions.
6. **Bounding Boxes** – highlights and counts moving objects.
7. **Display Feed** – shows live camera feed with motion status.
8. **Stop Key** – press `t` to stop execution.

---

## 📂 Project Structure

motion-detector/
├── motion_detector.py # Main script for motion detection
└── README.md # Project documentation

2. Install Dependencies
pip install opencv-python imutils
3. Run the Script
python motion_detector.py
Press t to stop the camera feed.

🧾 Code Highlights

cam = cv2.VideoCapture(0)        # Start camera
time.sleep(3)                    # Wait for camera to initialize
firstFrame = None
area = 500                       # Minimum contour area to detect
cv2.VideoCapture(0) → Opens default webcam

cv2.absdiff() → Detects difference between current and base frame

cv2.threshold() + cv2.dilate() → Isolate movement areas

cv2.findContours() → Find and track movement

cv2.rectangle() → Draw box around moving object

cv2.putText() → Show status and object count

