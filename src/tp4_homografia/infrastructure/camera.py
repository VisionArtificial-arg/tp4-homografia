import cv2
import numpy as np


class Camera:
    def __init__(self):
        self._capture = cv2.VideoCapture(0)

    def read(self) -> np.ndarray:

        success, frame = self._capture.read()

        if not success:
            raise RuntimeError("Camera read failed")

        return frame

    def release(self):

        self._capture.release()
