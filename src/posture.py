from ultralytics import YOLO
import numpy as np

class PostureClassifier:
    def __init__(self):
        self.pose_model = YOLO("yolov8n-pose.pt")

    def classify(self, frame, person_bbox):
        x1, y1, x2, y2 = person_bbox
        crop = frame[y1:y2, x1:x2]

        if crop.size == 0:
            return "unknown"

        results = self.pose_model(crop, verbose=False)

        for r in results:
            if r.keypoints is None:
                return "unknown"

            kp = r.keypoints.xy[0].cpu().numpy()

            if len(kp) < 17:
                return "unknown"

            shoulder_y = np.mean([kp[5][1], kp[6][1]])
            hip_y = np.mean([kp[11][1], kp[12][1]])
            knee_y = np.mean([kp[13][1], kp[14][1]])

            if hip_y < knee_y - 15:
                return "standing"
            elif hip_y > knee_y - 10:
                return "sitting"
            else:
                return "bending"

        return "unknown"
