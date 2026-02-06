import cv2
from src.detector import ObjectDetector
from src.posture import PostureClassifier
from src.visualizer import draw
from src.utils import side_by_side

video_path = "data/videos/test.mp4"
output_path = "outputs/videos/comparison.mp4"

cap = cv2.VideoCapture(video_path)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter(
    output_path,
    cv2.VideoWriter_fourcc(*"avc1"),
    fps,
    (w * 2, h)
)

if not out.isOpened():
    raise RuntimeError("VideoWriter failed to open")

detector = ObjectDetector()
posture_model = PostureClassifier()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    original = frame.copy()
    annotated = frame.copy()

    detections = detector.detect(annotated)
    postures = {}

    for det in detections:
        if det["label"] == "person":
            postures[det["bbox"]] = posture_model.classify(annotated, det["bbox"])

    annotated = draw(annotated, detections, postures)

    comparison = side_by_side(original, annotated)
    out.write(comparison)

cap.release()
out.release()

print(f"Saved side-by-side video to {output_path}")
