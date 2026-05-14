import cv2

from .states import VisualizationState
from .infrastructure import Camera


class Application:
    def __init__(self) -> None:
        self.camera = Camera()
        self.state = VisualizationState()
        self.running = True

    def run(self):
        while self.running:
            frame = self.camera.read()
            cv2.imshow("Perspective", frame)
            key = cv2.waitKey(1)

            if key == 27:
                self.running = False
        self.camera.release()
