from typing import Optional
import cv2

from tp4_homografia.domain.point import Point
from tp4_homografia.domain.state_machine.state_event import EndSelectionEvent

from .domain.homography import Homography
from .services.opencv import OpenCVHomographyService
from .interaction.input_controller import InputController
from .domain.state_machine import StateMachine
from .infrastructure import Camera


class Application:
    def __init__(self) -> None:
        self.camera = Camera()
        self.state_machine: StateMachine = StateMachine()
        self.homography_service = OpenCVHomographyService()
        self.last_homography: Optional[Homography] = None

    def run(self):
        frame = self.camera.read()
        cv2.imshow("Perspective", frame)
        self.input_controller: InputController = InputController(
            self.state_machine, "Perspective"
        )
        while self.state_machine.is_running():
            frame = self.camera.read()
            cv2.imshow("Perspective", frame)
            input_event = self.input_controller.poll()
            if isinstance(input_event, EndSelectionEvent):
                print("Doing Homography")
                destination = (
                    Point(0, 300),
                    Point(300, 0),
                    Point(300, 300),
                    Point(0, 300),
                )
                self.last_homography = self.homography_service.compute(
                    (input_event).corners, destination
                )

            self.state_machine.transition(input_event)
            update_event = self.state_machine.current.update(frame)
            self.state_machine.transition(update_event)
        self.camera.release()
