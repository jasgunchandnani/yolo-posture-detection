import cv2

def side_by_side(original, annotated):
    """
    Returns a side-by-side image (original | annotated)
    """
    if original.shape != annotated.shape:
        annotated = cv2.resize(
            annotated,
            (original.shape[1], original.shape[0])
        )

    return cv2.hconcat([original, annotated])
