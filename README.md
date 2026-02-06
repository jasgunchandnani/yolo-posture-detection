# YOLO Posture Detection

A computer vision project that uses **YOLOv8** to detect humans and classify their **posture** (e.g., standing, sitting, bending) from images and videos.

This project demonstrates how object detection models can be extended with simple posture analysis logic for real-world applications such as ergonomics monitoring, activity recognition, and surveillance.

---

## 📌 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Run on Image](#run-on-image)
  - [Run on Video](#run-on-video)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)
- [Contributors](#contributors)
- [License](#license)

---

## 📖 Introduction

**YOLO Posture Detection** is a Python-based application that uses the **YOLO (You Only Look Once)** object detection framework to identify humans in images and videos and classify their posture.

The project focuses on:
- Detecting people using YOLOv8
- Analyzing bounding box and pose-related information
- Classifying postures such as **standing**, **sitting**, or **bending**

---

## ✨ Features

- Real-time human detection using YOLOv8
- Posture classification (standing / sitting / bending)
- Supports both **image** and **video** inputs
- Modular and easy-to-extend codebase
- OpenCV-based visualization of results

---

## 📂 Project Structure

```

yolo-posture-detection/
│
├── data/                     # Sample images or data files
├── outputs/
│   └── images/               # Output images with posture annotations
├── src/                      # Source code modules
├── run_image.py              # Run posture detection on images
├── run_video.py              # Run posture detection on videos
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .gitignore

````

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/jasgunchandnani/yolo-posture-detection.git
cd yolo-posture-detection
````

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run on Image

```bash
python run_image.py
```

* Update the image path inside `run_image.py` if required
* Output images will be saved in the `outputs/images/` directory

---

### Run on Video

```bash
python run_video.py
```

* Supports video file input
* Can be extended for webcam or real-time streaming

---

## 📦 Dependencies

Key libraries used in this project include:

* Python 3.x
* Ultralytics YOLOv8
* OpenCV (`cv2`)
* NumPy

(See `requirements.txt` for the complete list.)

---

## 🔧 Configuration

* YOLO model weights can be changed in the scripts
* Input image/video paths can be modified in:

  * `run_image.py`
  * `run_video.py`
* Posture classification logic can be extended in the `src/` folder

---
### Sample Output

Here is an example output of the posture detection:

![Detection Result](https://github.com/jasgunchandnani/yolo-posture-detection/blob/main/outputs/images/comparison.jpg?raw=true)

---
## 🖼️ Examples

Example output includes:

* Bounding boxes around detected humans
* Text labels showing posture classification

Outputs are saved under:

```
outputs/images/
```

---

## 🛠️ Troubleshooting

**Model not loading**

* Ensure YOLOv8 is installed correctly
* Check internet access for first-time model download

**Low accuracy**

* Improve lighting and camera angle
* Use higher resolution input
* Extend posture logic using pose keypoints

**Import errors**

* Verify Python version
* Reinstall dependencies using `requirements.txt`

---

## 🚀 Future Improvements

* Add webcam/live stream support
* Use pose keypoints instead of bounding boxes
* Add more posture classes (lying down, leaning, running)
* Train a custom posture classification model
* Export results as CSV or JSON


---

## 📄 License

This project is licensed under the **MIT License**.
See the `LICENSE` file for more details.


