from typing import Any, Optional
import cv2


from .domain.point import Point
from .domain.state_machine.state_event import DetectQrEvent, EndSelectionEvent
from .domain.homography import Homography
from .services import OpenCVHomographyService, WarpRenderer, GridRenderer
from .services import OpenCVQRDetector
from .interaction.input_controller import InputController
from .domain.state_machine import StateMachine
from .infrastructure import Camera


class Application:
    def __init__(self) -> None:
        self.camera = Camera()
        self.state_machine: StateMachine = StateMachine()
        self.homography_service = OpenCVHomographyService()
        self.last_homography: Optional[Homography] = None
        self.last_homography_frame: Optional[Any] = None
        self.warp_renderer = WarpRenderer()
        self.grid_renderer = GridRenderer()
        self.qr_selector = OpenCVQRDetector()

    def run(self):
        cv2.namedWindow(
            "Perspective",
        )

        self.input_controller = InputController(
            self.state_machine,
            "Perspective",
        )

        while self.state_machine.is_running():
            frame = self.camera.read()
            input_event = self.input_controller.poll()
            if isinstance(input_event, DetectQrEvent):
                input_event = self.qr_selector.detect(frame)
            if isinstance(input_event, EndSelectionEvent):
                print("Doing Homography")
                destination = (
                    Point(0, 0),
                    Point(300, 0),
                    Point(300, 300),
                    Point(0, 300),
                )
                self.last_homography = self.homography_service.compute(
                    input_event.corners,
                    destination,
                )
                self.last_homography_frame = frame.copy()

            self.state_machine.transition(
                input_event,
            )
            update_event = self.state_machine.current.update(
                frame,
            )
            self.state_machine.transition(
                update_event,
            )
            if self.last_homography:
                self.warp_renderer.render(
                    self.last_homography_frame,
                    self.last_homography,
                )
                self.grid_renderer.render(
                    frame,
                    self.last_homography,
                )
            cv2.imshow(
                "Perspective",
                frame,
            )
        self.camera.release()
