import cv2
from src.detector import ObjectDetector
from src.posture import PostureClassifier
from src.visualizer import draw
from src.utils import side_by_side

image_path = "data/images/test.jpg"
output_path = "outputs/images/comparison.jpg"

detector = ObjectDetector()
posture_model = PostureClassifier()

original = cv2.imread(image_path)
annotated = original.copy()

detections = detector.detect(annotated)

postures = {}
for det in detections:
    if det["label"] == "person":
        postures[det["bbox"]] = posture_model.classify(annotated, det["bbox"])

annotated = draw(annotated, detections, postures)

comparison = side_by_side(original, annotated)

cv2.imwrite(output_path, comparison)
print(f"Saved side-by-side image to {output_path}")
