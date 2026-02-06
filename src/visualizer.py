import cv2

COLORS = {
    "standing": (0, 255, 0),
    "sitting": (255, 0, 0),
    "bending": (0, 0, 255),
    "person": (0, 255, 255)
}

def draw(frame, detections, postures):
    for det in detections:
        x1, y1, x2, y2 = det["bbox"]
        label = det["label"]

        box_color = COLORS.get(label, (255, 255, 255))

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)

        text = label
        if label == "person" and det["bbox"] in postures:
            text += f" ({postures[det['bbox']]})"

        # ---- Text styling ----
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale = 0.6
        thickness = 2

        (tw, th), _ = cv2.getTextSize(text, font, scale, thickness)

        # Background rectangle
        cv2.rectangle(
            frame,
            (x1, y1 - th - 12),
            (x1 + tw + 6, y1),
            (0, 0, 0),   # black background
            -1
        )

        # White text
        cv2.putText(
            frame,
            text,
            (x1 + 3, y1 - 6),
            font,
            scale,
            (255, 255, 255),
            thickness
        )

    return frame
