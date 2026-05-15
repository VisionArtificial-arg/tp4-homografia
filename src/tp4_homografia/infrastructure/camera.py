import cv2
import numpy as np


class Camera:
    def __init__(
        self,
    ) -> None:
        self._capture = cv2.VideoCapture(
            0,
            cv2.CAP_V4L2,
        )
        if not self._capture.isOpened():
            raise RuntimeError("Camera failed to open")
        self._capture.set(
            cv2.CAP_PROP_FOURCC,
            cv2.VideoWriter.fourcc(*"MJPG"),
        )
        self._capture.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            1280,
        )
        self._capture.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            720,
        )
        for _ in range(
            20,
        ):
            self._capture.read()
        print(
            self._capture.get(cv2.CAP_PROP_FRAME_WIDTH),
            self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT),
        )

    def read(self) -> np.ndarray:

        success, frame = self._capture.read()

        if not success:
            raise RuntimeError("Camera read failed")

        return frame

    def release(self):

        self._capture.release()
